import tensorflow as tf
tfk = tf.keras


# With extended batch shape [4, 7] (e.g. weather data where batch
# dimensions correspond to spatial location and the third dimension
# corresponds to time.)
input_shape = (4, 7, 10, 128)
x = tf.random.normal(input_shape)
y = tf.keras.layers.Conv1D(32, 3, activation='relu', input_shape=input_shape[2:])(x)
print(y.shape)