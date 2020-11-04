import numpy as np
import matplotlib.pyplot as plt

import torch


def eq_covariance(inputs1,
                  inputs2,
                  scale,
                  cov_coeff,
                  noise_coeff):
    
    diff = inputs1[:, :, None] - inputs2[:, None, :]
    
    quad = (diff / (2 * scale ** 2)) ** 2
    
    exp_quad = cov_coeff ** 2 * np.exp(- quad)
    
    return exp_quad


def sample_datasets_from_gps(low,
                             high,
                             batch_size,
                             num_train,
                             num_test,
                             scale,
                             cov_coeff,
                             noise_coeff,
                             as_tensor):
    
    x_train_test = np.random.uniform(low=low,
                                     high=high,
                                     size=(batch_size, num_train + num_test,))

    cov_train_test = eq_covariance(x_train_test,
                                   x_train_test,
                                   scale,
                                   cov_coeff,
                                   noise_coeff)
    
    cov_train_test = cov_train_test + noise_coeff ** 2 * np.eye(cov_train_test.shape[-1])[None, :, :]
    
    zeros = np.zeros((cov_train_test.shape[1],))
    noise = np.random.multivariate_normal(zeros, np.diag(np.ones_like(zeros)), size=(batch_size,))
    chol_train_test = np.linalg.cholesky(cov_train_test)
    
    y_train_test = np.einsum('bij, bj -> bi', chol_train_test, noise)
    
    x_train = x_train_test[:, :num_train, None]
    x_test = x_train_test[:, num_train:, None]
    
    y_train = y_train_test[:, :num_train, None]
    y_test = y_train_test[:, num_train:, None]
    
    
    x_train, y_train, x_test, y_test = [torch.tensor(array).float() if as_tensor else array \
                                        for array in (x_train, y_train, x_test, y_test)]
    
    return (x_train, y_train), (x_test, y_test)


def gp_post_pred(train_inputs,
                 train_outputs,
                 pred_inputs,
                 scale,
                 cov_coeff,
                 noise_coeff):
    
    K = eq_covariance(train_inputs,
                      train_inputs,
                      scale,
                      cov_coeff,
                      noise_coeff)[0]
    
    K = K + noise_coeff ** 2 * np.eye(K.shape[-1])
    
    k_star = eq_covariance(pred_inputs,
                           train_inputs,
                           scale,
                           cov_coeff,
                           noise_coeff)[0]
    
    means = np.dot(k_star, np.linalg.solve(K, train_outputs[0]))
    
    K_inv_k_star = np.linalg.solve(K, k_star.T)
    stds = (cov_coeff - np.diag(np.einsum('ij, jk -> ik', k_star, K_inv_k_star)) + noise_coeff ** 2) ** 0.5
    
    return means, stds


def cnp_plot_sample_and_predictions(conditional_neural_process,
                                    input_range,
                                    num_train,
                                    num_test,
                                    scale,
                                    cov_coeff,
                                    noise_coeff,
                                    step,
                                    plot_test_data=False):

    train_data, test_data = sample_datasets_from_gps(batch_size=1,
                                                     num_train=num_train,
                                                     num_test=num_test,
                                                     scale=scale,
                                                     cov_coeff=cov_coeff,
                                                     noise_coeff=noise_coeff,
                                                     as_tensor=True)

    context_inputs, context_outputs = train_data
    target_inputs = torch.linspace(input_range[0],
                                   input_range[1],
                                   100)[None, :]
    
    pred_mean, pred_log_stdev = conditional_neural_process.forward(context_inputs,
                                                                   context_outputs,
                                                                   target_inputs)
    
    gp_means, gp_stds = gp_post_pred(train_data[0],
                                     train_data[1],
                                     target_inputs,
                                     scale,
                                     cov_coeff,
                                     noise_coeff)
    
    target_inputs = target_inputs.squeeze().detach().numpy()
    pred_mean = pred_mean.squeeze().detach().numpy()
    pred_stdev = torch.exp(pred_log_stdev).squeeze().detach().numpy()
    
    plt.plot(target_inputs, gp_means, color='blue', zorder=1)
    plt.fill_between(target_inputs,
                     gp_means - gp_stds,
                     gp_means + gp_stds,
                     color='blue',
                     alpha=0.3,
                     zorder=1)
    
    plt.scatter(train_data[0],
                train_data[1],
                s=100,
                marker='x',
                color='black',
                label='Context (observed)')
    
    plt.plot(target_inputs,
             pred_mean,
             color='black')
    
    plt.fill_between(target_inputs,
                     pred_mean - pred_stdev,
                     pred_mean + pred_stdev,
                     color='gray',
                     alpha=0.3)
    
    if plot_test_data:
        plt.scatter(test_data[0], 
                    test_data[1], 
                    marker='x', 
                    color='red',
                    label='Target (unobserved)',
                    alpha=0.2,
                    zorder=1)

    plt.xlim([-6, 6])
    plt.ylim([-3, 3])
    plt.legend(loc='lower right')
    plt.title(f'Step {step}', fontsize=16)
    
    plt.show()
    
    
    
    
def np_plot_sample_and_predictions(neural_process,
                                   low,
                                   high,
                                   input_range,
                                   num_train,
                                   num_test,
                                   scale,
                                   cov_coeff,
                                   noise_coeff,
                                   step,
                                   plot_test_data=False):

    train_data, test_data = sample_datasets_from_gps(low=low,
                                                     high=high,
                                                     batch_size=1,
                                                     num_train=num_train,
                                                     num_test=num_test,
                                                     scale=scale,
                                                     cov_coeff=cov_coeff,
                                                     noise_coeff=noise_coeff,
                                                     as_tensor=True)

    context_inputs, context_outputs = train_data
    target_inputs = torch.linspace(input_range[0],
                                   input_range[1],
                                   100)[None, :, None]
    
    pred_mean, pred_stdev = neural_process.forward(context_inputs,
                                                   context_outputs,
                                                   target_inputs)
    
    gp_means, gp_stds = gp_post_pred(train_data[0][..., 0],
                                     train_data[1][..., 0],
                                     target_inputs[..., 0],
                                     scale,
                                     cov_coeff,
                                     noise_coeff)
    
    target_inputs = target_inputs.squeeze().detach().numpy()
    pred_mean = pred_mean.squeeze().detach().numpy()
    pred_stdev = pred_stdev.squeeze().detach().numpy()
    
    plt.plot(target_inputs, gp_means, color='blue', zorder=1)
    plt.fill_between(target_inputs,
                     gp_means - gp_stds,
                     gp_means + gp_stds,
                     color='blue',
                     alpha=0.3,
                     zorder=1)
    
    plt.scatter(train_data[0],
                train_data[1],
                s=100,
                marker='x',
                color='black',
                label='Context (observed)')
    
    plt.plot(target_inputs,
             pred_mean,
             color='black')
    
    plt.fill_between(target_inputs,
                     pred_mean - pred_stdev,
                     pred_mean + pred_stdev,
                     color='gray',
                     alpha=0.3)
    
    if plot_test_data:
        plt.scatter(test_data[0], 
                    test_data[1], 
                    marker='x', 
                    color='red',
                    label='Target (unobserved)',
                    alpha=0.2,
                    zorder=1)

    plt.xlim(input_range)
    plt.ylim([-3, 3])
    plt.legend(loc='lower right')
    plt.title(f'Step {step}', fontsize=16)
    
    plt.show()