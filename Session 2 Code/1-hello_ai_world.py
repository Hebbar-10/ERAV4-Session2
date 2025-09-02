import sys
import numpy as np
import torch

print("Hello, AI World!")
print(f"I'm using Python version: {__import__('sys').version.split()[0]}")
print(f"NumPy version: {np.__version__}")
print(f"PyTorch version: {torch.__version__}")

# Simple neural network using NumPy
def simple_nn(input_size, hidden_size, output_size):
    # Initialize weights and biases
    W1 = np.random.randn(input_size, hidden_size)
    W2 = np.random.randn(hidden_size, output_size)

    # Activation function
    def relu(x):
        return np.maximum(0, x)

    # Forward pass
    def forward(X):
        z1 = np.dot(X, W1)
        a1 = relu(z1)
        z2 = np.dot(a1, W2)
        return z2

    return forward

# Example usage
X = np.random.randn(1, 5)  # Input
model = simple_nn(5, 3, 2)
output = model(X)

print("Simple NN output:", output)

# Annotation: This script demonstrates a basic setup for AI development,
# including version checks for key libraries and a simple neural network implementation.