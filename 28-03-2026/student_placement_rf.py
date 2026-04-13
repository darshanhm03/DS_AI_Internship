# ==========================================
# STUDENT PLACEMENT RISK PREDICTION PROJECT
# ==========================================

# Phase 0: Import Libraries
import numpy as np
import pandas as pd
import time

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report, confusion_matrix

# For reproducibility
RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)

# ==========================================
# Phase 1: Data Architecture
# ==========================================

# Step 1: Generate synthetic student dataset
X, y = make_classification(
    n_samples=1000,              # 1000 students
    n_features=20,               # 20 features
    n_informative=12,
    n_redundant=4,
    n_repeated=0,
    n_classes=2,
    weights=[0.9, 0.1],          # 90% placed, 10% unplaced (minority class)
    flip_y=0.01,
    class_sep=1.0,
    random_state=RANDOM_STATE
)

# Feature names (student-like attributes)
feature_names = [
    "CGPA", "Internships", "Backlogs", "Projects", "AptitudeScore",
    "CommunicationSkill", "CodingSkill", "Attendance", "Hackathons",
    "TechnicalCertifications", "SoftSkills", "Teamwork", "Leadership",
    "ProblemSolving", "MockInterviewScore", "ResumeScore", "Extracurriculars",
    "Networking", "Discipline", "ResearchWork"
]

# Convert to DataFrame
df = pd.DataFrame(X, columns=feature_names)

# Target column: 1 = Placed, 0 = Unplaced
df["PlacementStatus"] = y

print("First 5 rows of dataset:")
print(df.head())
print("\nClass Distribution:")
print(df["PlacementStatus"].value_counts(normalize=True) * 100)

# Step 2: Split data (Golden Rule: 80/20)
X = df.drop("PlacementStatus", axis=1)
y = df["PlacementStatus"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,              # 80/20 split
    stratify=y,                 # maintain imbalance ratio
    random_state=RANDOM_STATE
)

print("\nTraining Set Shape:", X_train.shape)
print("Testing Set Shape:", X_test.shape)

# Step 3: Feature Scaling
# WARNING: Fit only on training data to avoid data leakage
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)   # fit only on train
X_test_scaled = scaler.transform(X_test)         # transform test only

# ==========================================
# Phase 2: Baseline & The "Metric Trap"
# ==========================================

print("\n" + "="*50)
print("PHASE 2: BASELINE MODEL")
print("="*50)

# Step 4: Baseline Random Forest
baseline_rf = RandomForestClassifier(random_state=RANDOM_STATE)
baseline_rf.fit(X_train_scaled, y_train)

y_pred_baseline = baseline_rf.predict(X_test_scaled)

baseline_accuracy = accuracy_score(y_test, y_pred_baseline)
baseline_f1 = f1_score(y_test, y_pred_baseline)

print(f"Baseline Accuracy: {baseline_accuracy:.4f}")
print(f"Baseline F1-Score: {baseline_f1:.4f}")

print("\nBaseline Classification Report:")
print(classification_report(y_test, y_pred_baseline))

print("Baseline Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_baseline))

# ==========================================
# Grid Search Parameters
# ==========================================

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10]
}

# ------------------------------------------
# Grid Search optimizing ACCURACY
# ------------------------------------------
print("\n" + "="*50)
print("GRID SEARCH OPTIMIZING FOR ACCURACY")
print("="*50)

rf_acc = RandomForestClassifier(random_state=RANDOM_STATE)

start_time_acc = time.time()

grid_acc = GridSearchCV(
    estimator=rf_acc,
    param_grid=param_grid,
    scoring='accuracy',
    cv=5,
    n_jobs=-1,
    verbose=1
)

grid_acc.fit(X_train_scaled, y_train)

end_time_acc = time.time()
grid_acc_time = end_time_acc - start_time_acc

best_model_acc = grid_acc.best_estimator_
y_pred_acc = best_model_acc.predict(X_test_scaled)

grid_acc_accuracy = accuracy_score(y_test, y_pred_acc)
grid_acc_f1 = f1_score(y_test, y_pred_acc)

print("\nBest Parameters (Accuracy):")
print(grid_acc.best_params_)

print(f"Best CV Accuracy: {grid_acc.best_score_:.4f}")
print(f"Test Accuracy: {grid_acc_accuracy:.4f}")
print(f"Test F1-Score: {grid_acc_f1:.4f}")
print(f"Execution Time: {grid_acc_time:.2f} seconds")

print("\nClassification Report (Accuracy-Optimized Model):")
print(classification_report(y_test, y_pred_acc))

# ------------------------------------------
# Grid Search optimizing F1-Score
# ------------------------------------------
print("\n" + "="*50)
print("GRID SEARCH OPTIMIZING FOR F1-SCORE")
print("="*50)

rf_f1 = RandomForestClassifier(random_state=RANDOM_STATE)

start_time_f1 = time.time()

grid_f1 = GridSearchCV(
    estimator=rf_f1,
    param_grid=param_grid,
    scoring='f1',
    cv=5,
    n_jobs=-1,
    verbose=1
)

grid_f1.fit(X_train_scaled, y_train)

end_time_f1 = time.time()
grid_f1_time = end_time_f1 - start_time_f1

best_model_f1 = grid_f1.best_estimator_
y_pred_f1 = best_model_f1.predict(X_test_scaled)

grid_f1_accuracy = accuracy_score(y_test, y_pred_f1)
grid_f1_f1 = f1_score(y_test, y_pred_f1)

print("\nBest Parameters (F1-Score):")
print(grid_f1.best_params_)

print(f"Best CV F1-Score: {grid_f1.best_score_:.4f}")
print(f"Test Accuracy: {grid_f1_accuracy:.4f}")
print(f"Test F1-Score: {grid_f1_f1:.4f}")
print(f"Execution Time: {grid_f1_time:.2f} seconds")

print("\nClassification Report (F1-Optimized Model):")
print(classification_report(y_test, y_pred_f1))

# ==========================================
# Phase 3: Efficiency Warfare
# ==========================================

print("\n" + "="*50)
print("PHASE 3: EFFICIENCY WARFARE")
print("="*50)

# Randomized Search with wider range
param_dist = {
    'n_estimators': np.arange(10, 501, 10),   # 10 to 500
    'max_depth': [None] + list(np.arange(5, 31, 5)),
    'min_samples_split': np.arange(2, 21, 2)
}

rf_random = RandomForestClassifier(random_state=RANDOM_STATE)

start_time_random = time.time()

random_search = RandomizedSearchCV(
    estimator=rf_random,
    param_distributions=param_dist,
    n_iter=20,
    scoring='f1',
    cv=5,
    random_state=RANDOM_STATE,
    n_jobs=-1,
    verbose=1
)

random_search.fit(X_train_scaled, y_train)

end_time_random = time.time()
random_time = end_time_random - start_time_random

best_random_model = random_search.best_estimator_
y_pred_random = best_random_model.predict(X_test_scaled)

random_accuracy = accuracy_score(y_test, y_pred_random)
random_f1 = f1_score(y_test, y_pred_random)

print("\nBest Parameters (Randomized Search):")
print(random_search.best_params_)

print(f"Best CV F1-Score: {random_search.best_score_:.4f}")
print(f"Test Accuracy: {random_accuracy:.4f}")
print(f"Test F1-Score: {random_f1:.4f}")
print(f"Execution Time: {random_time:.2f} seconds")

print("\nClassification Report (Randomized Search Model):")
print(classification_report(y_test, y_pred_random))

# ==========================================
# Final Comparison Table
# ==========================================

print("\n" + "="*50)
print("FINAL COMPARISON TABLE")
print("="*50)

comparison_df = pd.DataFrame({
    "Model": [
        "Baseline Random Forest",
        "Grid Search (Accuracy)",
        "Grid Search (F1-Score)",
        "Randomized Search (F1-Score)"
    ],
    "Best Parameters": [
        "Default",
        str(grid_acc.best_params_),
        str(grid_f1.best_params_),
        str(random_search.best_params_)
    ],
    "Test Accuracy": [
        round(baseline_accuracy, 4),
        round(grid_acc_accuracy, 4),
        round(grid_f1_accuracy, 4),
        round(random_accuracy, 4)
    ],
    "Test F1-Score": [
        round(baseline_f1, 4),
        round(grid_acc_f1, 4),
        round(grid_f1_f1, 4),
        round(random_f1, 4)
    ],
    "Time Taken (sec)": [
        0,   # baseline time ignored
        round(grid_acc_time, 2),
        round(grid_f1_time, 2),
        round(random_time, 2)
    ]
})

print(comparison_df)

# Save results if needed
comparison_df.to_csv("student_placement_model_comparison.csv", index=False)

print("\nResults saved to: student_placement_model_comparison.csv")