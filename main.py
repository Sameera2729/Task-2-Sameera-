import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Sample dataset
data = {
    "StudyHours":[8,7,2,5,9,3,6,4,8,1,7,2,9,5,6],
    "Attendance":[95,88,60,75,98,65,85,70,92,50,89,58,97,78,83],
    "AssignmentScore":[90,85,50,70,96,55,80,65,89,40,84,48,95,72,79],
    "TestScore":[88,82,45,72,94,50,78,60,90,35,81,42,93,70,76],
    "Performance":[
        "High","High","Low","Medium","High",
        "Low","Medium","Medium","High","Low",
        "High","Low","High","Medium","Medium"
    ]
}

df = pd.DataFrame(data)

X = df.drop("Performance", axis=1)
y = df["Performance"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\n===== EDUVISION AI REPORT =====")
print(f"Model Accuracy: {accuracy*100:.2f}%")

print("\nClassification Report:")
print(classification_report(y_test, predictions))

print("\nFeature Importance:")

importance = model.feature_importances_

for feature, score in zip(X.columns, importance):
    print(f"{feature}: {score:.3f}")

print("\n===== STUDENT RISK ANALYZER =====")

new_student = [[3, 60, 50, 45]]

result = model.predict(new_student)[0]

print("Prediction:", result)

if result == "Low":
    print("⚠ High Academic Risk Detected")
    print("Recommendation:")
    print("- Increase study hours")
    print("- Improve attendance")
    print("- Submit assignments on time")
elif result == "Medium":
    print("Moderate Risk")
    print("Recommendation:")
    print("- Practice weekly tests")
    print("- Improve consistency")
else:
    print("Excellent Performance Expected")