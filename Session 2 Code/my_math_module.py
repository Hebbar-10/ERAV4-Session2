import numpy as np

def add(a, b):
    return np.add(a, b)  # Using NumPy for potential array operations

def multiply(a, b):
    return np.multiply(a, b)  # Using NumPy for potential array operations

def matrix_multiply(A, B):
    return np.dot(A, B)  # Matrix multiplication, crucial for neural network operations

def relu(x):
    return np.maximum(0, x)  # ReLU activation function, commonly used in neural networks

def sigmoid(x):
    return 1 / (1 + np.exp(-x))  # Sigmoid activation function, used in logistic regression and neural networks

PI = np.pi  # Using NumPy's more precise value of pi

# Annotation: These functions demonstrate basic mathematical operations used in ML,
# including activation functions for neural networks and matrix operations.