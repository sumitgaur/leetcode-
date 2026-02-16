import numpy as np
from sklearn.linear_model import LinearRegression


def linear_regression():
    global X, y, model, X_new, prediction
    # 1. Define Sample Data
    # X is the feature (input), y is the target (output)
    # X needs to be a 2D array (n_samples, n_features)
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([1.5, 3.1, 4.5, 6.2, 7.9])
    # 2. Initialize the Model (Estimator)
    model = LinearRegression()
    # 3. Fit the Model (Training Phase)
    # The model learns the relationship between X and y (calculates the slope and intercept)
    model.fit(X, y)
    # 4. Make a Prediction
    # Predict the target value for a new input, e.g., X_new = 6
    X_new = np.array([[6]])
    prediction = model.predict(X_new)



if __name__ == '__main__':
    linear_regression()
    # Print the results
    print(f"Input data (X):\n{X}")
    print(f"Target data (y):\n{y}")
    print(f"New input for prediction (X_new): {X_new.flatten()}")
    print(f"Predicted value: {prediction.flatten()[0]:.2f}")


