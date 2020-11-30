from minimize import *
import autograd.numpy as np
import matplotlib.pyplot as plt


# =============================================================================
# Plotting helpers
# =============================================================================

            
def line_post_pred(t_data, ms, Vs, iVC, num_points=100):

    tdiff = t_data[-1] - t_data[0]
    tmin = t_data[0] + tdiff * 1e-2
    tmax = t_data[-1] + 0.5 * tdiff
    
    t = np.linspace(tmin, tmax, num_points)
    
    mean, var = list(zip(*[post_pred(t_, t_data, ms, Vs, iVC) for t_ in t]))
    
    mean = np.array(mean)
    var = np.array(var)
            
    return t, mean, var
            
            
def plot_linesearch(c1,
                    c2,
                    t_data,
                    mf,
                    Vf,
                    ms,
                    Vs,
                    iVC,
                    post_probs,
                    wp_probs,
                    x=None,
                    y=None,
                    options=None):
    
    plt.figure(figsize=(14, 9))
    
    # Filtered posteriors
    mf_average = np.sum(np.array(mf) * post_probs[:, None], axis=0)
    Vf_average = np.sum(np.array(Vf) * post_probs[:, None, None], axis=0)
    
    # Smoothed posteriors
    ms_average = np.sum(np.array(ms) * post_probs[:, None], axis=0)
    Vs_average = np.sum(np.array(Vs) * post_probs[:, None, None], axis=0)
    
    # Interpolated/extrapolated posterior
    posteriors = list(zip(*[line_post_pred(t_data, ms_, Vs_, iVC_) \
                            for ms_, Vs_, iVC_ in zip(ms, Vs, iVC)]))
    
    t, m, v = posteriors
    t = t[0]
    m = np.sum(np.array(m) * post_probs[:, None], axis=0)
    v = np.sum(np.array(v) * post_probs[:, None, None], axis=0)
    
    ms = np.sum(np.array(ms) * post_probs[:, None], axis=0)
    
    ymin = np.min(y, axis=0)
    ymax = np.max(y, axis=0)
    yrange = ymax - ymin
    ymin = ymin - 4e-1 * yrange
    ymax = ymax + 4e-1 * yrange
    
    tmin = np.min(t, axis=0)
    tmax = np.max(t, axis=0)
    trange = tmax - tmin

    for i in range(3):
    
        # Plot smootthed posterior
        plt.subplot(3, 4, 4 * i + 1)

        if not(x is None):
            plt.scatter(t_data, x[:, i], marker='x', color='blue', label=r'$x_{}$'.format(i+1))

        if i < 2:
            plt.scatter(t_data, y[:, i], marker='x', color='red', label=r'$y_{}$'.format(i+1))
            
        if i == 0:
            
            if not (options is None):
                kfs_info = options['kfs_info']
                plt.title('Filtered posterior (KFS)\n' + kfs_info, fontsize=16)
                
            else:
                plt.title('Filtered posterior (KFS)', fontsize=16)
                

        plt.errorbar(x=t_data,
                     y=mf_average[:, i],
                     yerr=Vf_average[:, i, i] ** 0.5,
                     color='black',
                     zorder=2,
                     fmt="none",
                     label=r"$m_t^t \pm \sqrt{V_t^T}$",
                     capsize=4)
        
        plt.xlabel(r'$t$', fontsize=16)
        plt.legend(loc='upper right')

        if i == 0:
            plt.ylabel(r'$f$', fontsize=16)
        if i == 1:
            plt.ylabel(r"$f'$", fontsize=16)
        if i == 2:
            plt.ylabel(r"$f''$", fontsize=16)
    
        # Plot smootthed posterior
        plt.subplot(3, 4, 4 * i + 2)

        if not(x is None):
            plt.scatter(t_data, x[:, i], marker='x', color='blue', label=r'$x_{}$'.format(i+1))

        if i < 2:
            plt.scatter(t_data, y[:, i], marker='x', color='red', label=r'$y_{}$'.format(i+1))
            
        if i == 0:
            
            if not (options is None):
                kfs_info = options['kfs_info']
                plt.title('Smoothed posterior (KFS)\n' + kfs_info, fontsize=16)
                
            else:
                plt.title('Smoothed posterior (KFS)', fontsize=16)
                

        plt.errorbar(x=t_data,
                     y=ms_average[:, i],
                     yerr=Vs_average[:, i, i] ** 0.5,
                     color='black',
                     zorder=2,
                     fmt="none",
                     label=r"$m_t^t \pm \sqrt{V_t^T}$",
                     capsize=4)
        
        plt.xlabel(r'$t$', fontsize=16)
        plt.legend(loc='upper right')
            

        # Plot Quintic Spline posterior
        plt.subplot(3, 4, 4 * i + 3)

        plt.plot(t, m[:, i], color='k')
        
        if not(x is None):
            plt.scatter(t_data,
                        x[:, i],
                        marker='x',
                        color='blue',
                        label=r'$x_{}$'.format(i+1))

        if i < 2:
            plt.scatter(t_data,
                        y[:, i],
                        marker='x',
                        color='red',
                        label=r'$y_{}$'.format(i+1))

        plt.fill_between(t,
                         m[:, i] - v[:, i, i] ** 0.5,
                         m[:, i] + v[:, i, i] ** 0.5,
                         color='gray', alpha=0.5)
        
        plt.xlabel(r'$t$', fontsize=16)
        if i < 2 or not (x is None): plt.legend(loc='upper right')
            
#         if i < 2:
#             plt.ylim([ymin[i], ymax[i]])

        if i == 0:
            plt.title('Smoothed posterior', fontsize=16)


        # Plot WP acceptance probabilities
        if i < 2:

            plt.subplot(3, 4, 4 * i + 4)

            if i == 0:
                wp_line = ms[0, 0] + t * c1 * ms[0, 1]
                plt.plot(t, wp_line, '--', color='k')

            else:
                wp_line1 = c2 * np.abs(ms[0, 1]) * np.ones_like(t)
                wp_line2 = - c2 * np.abs(ms[0, 1]) * np.ones_like(t)
                
                plt.plot(t, wp_line1, '--', color='k')
                plt.plot(t, wp_line2, '--', color='k')

            if not (x is None):
                plt.scatter(t_data,
                            x[:, i],
                            marker='x',
                            color='blue',
                            label=r'$x_{}$'.format(i+1))
                
            plt.title('EI and WP acceptance probs', fontsize=16)

            plt.plot(t, m[:, i], color='k')
            plt.fill_between(t,
                             m[:, i] - v[:, i, i] ** 0.5,
                             m[:, i] + v[:, i, i] ** 0.5,
                             color='gray', alpha=0.5)

            plt.xlabel(r'$t$', fontsize=16)
            if not (x is None): plt.legend(loc='upper right')
            
#             if i < 2:
#                 plt.ylim([ymin[i], ymax[i]])

            ax2 = plt.gca().twinx()
            ax2.bar(t_data[1:],
                    height=wp_probs,
                    width=(trange/100),
                    color='green',
                    alpha=0.2,
                    linewidth=1,
                    edgecolor='black',
                    label='WP acc. prob.')

            plt.legend(loc='lower left')
            plt.ylim([0, 1])

    plt.tight_layout()
    
    if not (options is None):
        plt.savefig(options['save_path'])
        
    plt.show()