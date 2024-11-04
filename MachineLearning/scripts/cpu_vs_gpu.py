import os
import tensorflow as tf
import time
import numpy as np

tf.get_logger().setLevel('ERROR')

# Check if GPU is available
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    print(f"Using GPU: {gpus[0]}")
else:
    print("Using CPU")

# Define a function to measure execution time
def measure_time(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return result, elapsed_time

# Create a large dataset
X = np.random.rand(1000000, 10)
y = np.random.rand(1000000)

# Define a function to perform a computationally intensive task
def compute_dense_layer(X, y):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(1024, input_shape=(10,), activation='relu'),
        tf.keras.layers.Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    model.fit(X, y, epochs=5, batch_size=32)

# Measure execution time on CPU
print('Measuring CPU')
with tf.device('/CPU:0'):
    cpu_result, cpu_time = measure_time(compute_dense_layer, X, y)

# Measure execution time on GPU (if available)
print('Measuring GPU')
if gpus:
    with tf.device('/GPU:0'):
        gpu_result, gpu_time = measure_time(compute_dense_layer, X, y)

# Compare results
print("CPU time:", cpu_time)
print("GPU time:", gpu_time)
if gpus:
    print("Speedup:", cpu_time / gpu_time)
