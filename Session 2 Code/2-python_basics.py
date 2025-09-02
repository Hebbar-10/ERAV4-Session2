import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Basic variable types
integer_var = 42
float_var = 3.14159
string_var = "Artificial Intelligence"
boolean_var = True

print(f"Variable types: {type(integer_var)}, {type(float_var)}, {type(string_var)}, {type(boolean_var)}")

# Advanced data structures
# Lists and list comprehensions (useful for storing and manipulating data in ML)
data = [x**2 for x in range(100) if x % 2 == 0]
print(f"Squared even numbers: {data[:5]}...")

# Dictionaries (often used for feature engineering and storing model hyperparameters)
model_params = {
    'learning_rate': 0.01,
    'epochs': 100,
    'batch_size': 32,
    'activation': 'relu'
}

# Control flow with AI-related example
def evaluate_model_performance(accuracy):
    if accuracy > 0.95:
        return "Excellent performance, but check for overfitting"
    elif 0.8 <= accuracy <= 0.95:
        return "Good performance"
    else:
        return "Poor performance, consider tuning hyperparameters"

print(evaluate_model_performance(0.97))

# Functions and lambda expressions (useful for custom loss functions or data transformations)
def custom_activation(x, alpha=0.01):
    return np.maximum(alpha * x, x)

relu = lambda x: np.maximum(0, x)

# Numpy operations (fundamental for numerical computations in ML)
X = np.random.randn(100, 5)  # Generate random feature matrix
y = np.random.randint(0, 2, 100)  # Generate random binary labels

# Data preprocessing (common step in ML pipelines)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Matplotlib for data visualization (crucial for data analysis and model evaluation)
plt.figure(figsize=(10, 6))
plt.scatter(X_train_scaled[:, 0], X_train_scaled[:, 1], c=y_train, cmap='viridis')
plt.title("Feature Space Visualization")
plt.xlabel("Feature 1 (scaled)")
plt.ylabel("Feature 2 (scaled)")
plt.colorbar(label='Class')
plt.savefig('feature_visualization.png')
plt.close()

print("Feature visualization saved as 'feature_visualization.png'")

# Annotation: This script demonstrates basic Python concepts and their applications in ML,
# including data preprocessing, visualization, and simple model evaluation logic.
# These concepts form the foundation for more advanced ML topics like neural networks and deep learning.