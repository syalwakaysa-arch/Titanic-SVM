
import pandas as pd
import numpy as np
import joblib
import json
import os

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

# =====================================
# 1. MEMBACA DATASET
# =====================================

print("Membaca dataset Titanic...")

df = pd.read_csv("titanic.csv")

print("Dataset berhasil dibaca!")
print("Ukuran dataset:", df.shape)

# =====================================
# 2. PEMBERSIHAN DATA
# =====================================

print("\nMemeriksa dataset...")

# Menghapus baris yang tidak memiliki target
df = df.dropna(subset=["Survived"])

# Memilih fitur
features = [
    "Pclass",
    "Sex",
    "Age",
    "SibSp",
    "Parch",
    "Fare",
    "Embarked"
]

X = df[features]
y = df["Survived"].astype(int)

print("Jumlah missing values:")
print(X.isnull().sum())

# =====================================
# 3. PREPROCESSING DATA
# =====================================

numeric_features = [
    "Pclass",
    "Age",
    "SibSp",
    "Parch",
    "Fare"
]

categorical_features = [
    "Sex",
    "Embarked"
]

numeric_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer(transformers=[
    ("num", numeric_transformer, numeric_features),
    ("cat", categorical_transformer, categorical_features)
])

# =====================================
# 4. MEMBAGI DATA TRAINING DAN TESTING
# =====================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nJumlah data training:", len(X_train))
print("Jumlah data testing:", len(X_test))

# =====================================
# 5. MEMBUAT MODEL SVM
# =====================================

model = Pipeline(steps=[
    ("preprocessing", preprocessor),
    ("classifier", SVC(
        kernel="rbf",
        C=1.0,
        gamma="scale"
    ))
])

print("\nMelatih model SVM...")

model.fit(X_train, y_train)

print("Model SVM berhasil dilatih!")

# =====================================
# 6. EVALUASI MODEL
# =====================================

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(
    y_test, y_pred, zero_division=0
)
recall = recall_score(
    y_test, y_pred, zero_division=0
)
f1 = f1_score(
    y_test, y_pred, zero_division=0
)

cm = confusion_matrix(y_test, y_pred)

print("\n===== HASIL EVALUASI SVM =====")
print("Accuracy :", round(accuracy * 100, 2), "%")
print("Precision:", round(precision * 100, 2), "%")
print("Recall   :", round(recall * 100, 2), "%")
print("F1-Score :", round(f1 * 100, 2), "%")

print("\nConfusion Matrix:")
print(cm)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# =====================================
# 7. MENYIMPAN MODEL
# =====================================

os.makedirs("models", exist_ok=True)

joblib.dump(model, "models/svm_titanic.joblib")

# Menyimpan hasil evaluasi
report = classification_report(
    y_test,
    y_pred,
    target_names=["Tidak Selamat", "Selamat"],
    output_dict=True,
    zero_division=0
)

evaluation = {
    "accuracy": float(accuracy),
    "precision": float(precision),
    "recall": float(recall),
    "f1_score": float(f1),
    "confusion_matrix": cm.tolist(),
    "classification_report": report,
    "test_size": int(len(X_test)),
    "train_size": int(len(X_train))
}

with open("models/evaluation.json", "w") as file:
    json.dump(evaluation, file, indent=4)

print("\nModel berhasil disimpan!")
print("Lokasi: models/svm_titanic.joblib")
print("Hasil evaluasi: models/evaluation.json")
