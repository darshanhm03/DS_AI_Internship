import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

# Reproducibility
np.random.seed(42)

# -----------------------------
# ✅ Create Non-Linear Data
# -----------------------------
X = np.random.rand(200, 1) * 10   # Feature
y = X**2 + np.random.randn(200, 1) * 5  # Non-linear target + noise

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# ✅ Model 1: Simple Linear Regression
# -----------------------------
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

y_pred_linear = linear_model.predict(X_test)

r2_linear = r2_score(y_test, y_pred_linear)

print("R² Score (Linear Features):", r2_linear)

# -----------------------------
# ✅ Model 2: Polynomial Features (degree=2)
# -----------------------------
poly = PolynomialFeatures(degree=2)

X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)

y_pred_poly = poly_model.predict(X_test_poly)

r2_poly = r2_score(y_test, y_pred_poly)

print("R² Score (Polynomial Features):", r2_poly)
