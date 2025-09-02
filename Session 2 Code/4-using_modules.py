import my_math_module as mm
import numpy as np

# Basic operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result_add = mm.add(a, b)
result_multiply = mm.multiply(a, b)

print(f"Vector addition: {result_add}")
print(f"Element-wise multiplication: {result_multiply}")

# Matrix operations
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

result_matrix_multiply = mm.matrix_multiply(A, B)
print(f"Matrix multiplication:\n{result_matrix_multiply}")

# Activation functions
x = np.array([-2, -1, 0, 1, 2])
print(f"ReLU of {x}: {mm.relu(x)}")
print(f"Sigmoid of {x}: {mm.sigmoid(x)}")

print(f"PI is approximately {mm.PI}")

# Annotation: This script demonstrates how custom modules can be used in ML contexts,
# showcasing vector and matrix operations, as well as common activation functions.