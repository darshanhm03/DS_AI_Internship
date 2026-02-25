# Day23_Iris_Model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# 1️⃣ Load Dataset
df = pd.read_csv("iris.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

# 2️⃣ Separate Features and Target
X = df.iloc[:, :-1]   # all columns except last
y = df.iloc[:, -1]    # last column (species)

# 3️⃣ Convert Target Labels to Numbers
le = LabelEncoder()
y = le.fit_transform(y)

# 4️⃣ Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5️⃣ Train Model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 6️⃣ Make Predictions
y_pred = model.predict(X_test)

# 7️⃣ Evaluate Model
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# 8️⃣ Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

plt.figure()
sns.heatmap(cm, annot=True, fmt="d")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()