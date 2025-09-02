import numpy as np
import time

# Basic array creation (fundamental for representing data in ML)
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.zeros((4, 4))
arr3 = np.ones((2, 4))
arr4 = np.random.randn(1000, 1000)  # Large random matrix, useful for simulating high-dimensional data

print("Basic arrays:")
print(arr1, arr2, arr3)
print(f"Large random matrix shape: {arr4.shape}")

# Array operations (essential for efficient computations in ML algorithms)
print("\nArray operations:")
print("Element-wise multiplication:", arr1 * 2)
print("Matrix multiplication:", np.dot(arr2, arr3.T))

# Broadcasting (powerful feature for working with arrays of different shapes)
broadcast_example = arr1[:, np.newaxis] + np.arange(3)
print("\nBroadcasting example:")
print(broadcast_example)

# Advanced indexing (useful for feature selection and data manipulation)
complex_index = np.array([0, 2, 1, 4])
print("\nAdvanced indexing:")
print(arr1[complex_index])

# Vectorized operations (crucial for performance in ML)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Time comparison: vectorized vs loop
start_time = time.time()
vectorized_result = sigmoid(arr4)
vectorized_time = time.time() - start_time

start_time = time.time()
loop_result = np.zeros_like(arr4)
for i in range(arr4.shape[0]):
    for j in range(arr4.shape[1]):
        loop_result[i, j] = sigmoid(arr4[i, j])
loop_time = time.time() - start_time

print(f"\nVectorized operation time: {vectorized_time:.4f} seconds")
print(f"Loop operation time: {loop_time:.4f} seconds")
print(f"Speedup: {loop_time / vectorized_time:.2f}x")

# Linear algebra operations (fundamental for many ML algorithms)
A = np.random.randn(100, 100)
b = np.random.randn(100)

# Solving linear system Ax = b
x = np.linalg.solve(A, b)
print("\nLinear algebra:")
print(f"Solution to Ax = b, first 5 elements: {x[:5]}")

# Eigendecomposition (used in PCA, spectral clustering, etc.)
eigenvalues, eigenvectors = np.linalg.eig(A)
print(f"First 5 eigenvalues: {eigenvalues[:5]}")

# Annotation: NumPy forms the backbone of numerical computing in Python and is essential for ML.
# The concepts demonstrated here, such as efficient array operations, broadcasting, and linear algebra,
# are used extensively in implementing ML algorithms, from basic linear regression to complex neural networks.