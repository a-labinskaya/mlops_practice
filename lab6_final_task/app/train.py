import os
import joblib
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
MODEL_DIR = os.path.join(BASE_DIR, "app", "model")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(MODEL_DIR, exist_ok=True)

iris = load_iris(as_frame=True)
df = iris.frame

data_path = os.path.join(DATA_DIR, "iris.csv")
df.to_csv(data_path, index=False)

X = df.drop(columns=["target"])
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

model_path = os.path.join(MODEL_DIR, "model.pkl")
joblib.dump(model, model_path)

metrics_path = os.path.join(BASE_DIR, "metrics.txt")
with open(metrics_path, "w", encoding="utf-8") as file:
    file.write(f"accuracy={accuracy:.4f}\n")

print(f"Dataset saved to: {data_path}")
print(f"Model saved to: {model_path}")
print(f"Accuracy: {accuracy:.4f}")
