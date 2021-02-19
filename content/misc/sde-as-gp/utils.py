import tensorflow as tf


def sample_data_from_ou_gp(x, gamma, sigma):

    diff = (x[:, None] - x[None, :])
    cov = 0.5 * sigma ** 2 / gamma * tf.exp(- gamma * tf.abs(diff))

    chol = tf.linalg.cholesky(cov)
    rand = tf.random.normal(mean=0., stddev=1.0, shape=x.shape)
    y = tf.tensordot(chol, rand, axes=[[1], [0]])

    return y