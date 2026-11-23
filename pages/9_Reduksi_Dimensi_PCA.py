
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


# ==========================
# MEMUAT DATASET
# ==========================

@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    return pd.read_csv(url)


st.title("Reduksi Dimensi (PCA)")
st.write(
    "Penerapan Principal Component Analysis (PCA) "
    "pada dataset Titanic dengan mempertahankan 90% variansi."
)

st.markdown("---")

try:
    df = load_data()
except Exception as e:
    st.error(f"Gagal memuat dataset: {e}")
    st.stop()


# ==========================
# 1. DATASET
# ==========================

st.subheader("1. Memuat Dataset Titanic")

col1, col2 = st.columns(2)

with col1:
    st.metric("Jumlah Data", df.shape[0])

with col2:
    st.metric("Jumlah Fitur Awal", df.shape[1])

with st.expander("Lihat 5 data pertama"):
    st.dataframe(df.head(), use_container_width=True)


# ==========================
# 2. TRAIN TEST SPLIT
# ==========================

st.subheader("2. Pembagian Data Train dan Test")

X = df.drop(columns=["Survived"])
y = df["Survived"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

col1, col2 = st.columns(2)

with col1:
    st.metric("Data Training", X_train.shape[0])

with col2:
    st.metric("Data Testing", X_test.shape[0])

st.info(
    "Pembagian data dilakukan sebelum preprocessing "
    "untuk mencegah data leakage."
)


# ==========================
# 3. PREPROCESSING
# ==========================

st.subheader("3. Preprocessing Data")

X_train = X_train.drop(
    columns=["Cabin", "PassengerId", "Name", "Ticket"]
)

X_test = X_test.drop(
    columns=["Cabin", "PassengerId", "Name", "Ticket"]
)

numeric_features = [
    "Age", "Fare", "SibSp", "Parch", "Pclass"
]

categorical_features = [
    "Sex", "Embarked"
]

numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("num", numeric_pipeline, numeric_features),
    ("cat", categorical_pipeline, categorical_features)
])

X_train_scaled = preprocessor.fit_transform(X_train)
X_test_scaled = preprocessor.transform(X_test)

st.success("Preprocessing berhasil dilakukan.")

st.write("**Strategi preprocessing:**")

st.markdown("""
- Age: imputasi median.
- Embarked: imputasi modus.
- Cabin, PassengerId, Name, dan Ticket: dihapus.
- Sex dan Embarked: One-Hot Encoding.
- Fare, Age, SibSp, Parch, dan Pclass: StandardScaler.
""")

col1, col2 = st.columns(2)

with col1:
    st.metric("Fitur Sebelum PCA", X_train_scaled.shape[1])

with col2:
    st.metric("Jumlah Data Training", X_train_scaled.shape[0])


# ==========================
# 4. PCA
# ==========================

st.subheader("4. Reduksi Dimensi dengan PCA")

pca = PCA(n_components=0.90, random_state=42)

X_train_pca = pca.fit_transform(X_train_scaled)
X_test_pca = pca.transform(X_test_scaled)

n_components = pca.n_components_
explained = pca.explained_variance_ratio_
cumulative = np.cumsum(explained)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Fitur Sebelum PCA", X_train_scaled.shape[1])

with col2:
    st.metric("Komponen Setelah PCA", n_components)

with col3:
    st.metric(
        "Variansi Kumulatif",
        f"{cumulative[-1] * 100:.2f}%"
    )

st.write("**Perbandingan bentuk data:**")

comparison = pd.DataFrame({
    "Tahapan": ["Sebelum PCA", "Sesudah PCA"],
    "Data Training": [
        X_train_scaled.shape[0],
        X_train_pca.shape[0]
    ],
    "Jumlah Fitur": [
        X_train_scaled.shape[1],
        X_train_pca.shape[1]
    ]
})

st.dataframe(comparison, use_container_width=True)

st.write("**Scree Plot PCA Titanic**")

fig, ax = plt.subplots(figsize=(9, 4))

ax.plot(
    range(1, len(cumulative) + 1),
    cumulative,
    marker="o"
)

ax.axhline(
    y=0.90,
    color="red",
    linestyle="--",
    label="Target Variansi 90%"
)

ax.set_title("Cumulative Explained Variance PCA")
ax.set_xlabel("Jumlah Principal Component")
ax.set_ylabel("Cumulative Explained Variance")
ax.grid(True)
ax.legend()

st.pyplot(fig)
plt.close(fig)


# ==========================
# 5. LOGISTIC REGRESSION
# ==========================

st.subheader("5. Integrasi PCA dengan Logistic Regression")

model = LogisticRegression(
    max_iter=1000,
    random_state=42
)

model.fit(X_train_pca, y_train)

y_pred = model.predict(X_test_pca)

acc = accuracy_score(y_test, y_pred)

st.metric("Accuracy Model dengan PCA", f"{acc:.4f}")

report = classification_report(
    y_test,
    y_pred,
    output_dict=True,
    zero_division=0
)

report_df = pd.DataFrame(report).transpose()

st.write("**Classification Report**")
st.dataframe(report_df, use_container_width=True)


# ==========================
# 6. PERBANDINGAN MODEL
# ==========================

st.subheader("6. Perbandingan Sebelum dan Sesudah PCA")

model_before = LogisticRegression(
    max_iter=1000,
    random_state=42
)

model_before.fit(X_train_scaled, y_train)

pred_before = model_before.predict(X_test_scaled)

acc_before = accuracy_score(y_test, pred_before)

result = pd.DataFrame({
    "Metode": [
        "Tanpa PCA",
        "Dengan PCA"
    ],
    "Accuracy": [
        acc_before,
        acc
    ]
})

col1, col2 = st.columns(2)

with col1:
    st.metric("Accuracy Tanpa PCA", f"{acc_before:.4f}")

with col2:
    st.metric("Accuracy Dengan PCA", f"{acc:.4f}")

st.dataframe(result, use_container_width=True)

fig, ax = plt.subplots(figsize=(8, 4))

ax.bar(
    result["Metode"],
    result["Accuracy"]
)

ax.set_title("Perbandingan Accuracy Sebelum dan Sesudah PCA")
ax.set_ylabel("Accuracy")
ax.set_ylim(0, 1)
ax.grid(axis="y", alpha=0.3)

st.pyplot(fig)
plt.close(fig)


# ==========================
# 7. KESIMPULAN
# ==========================

st.subheader("7. Kesimpulan")

st.write(
    f"""
    PCA berhasil mereduksi jumlah fitur dari
    **{X_train_scaled.shape[1]} fitur** menjadi
    **{n_components} principal component** dengan
    mempertahankan **{cumulative[-1] * 100:.2f}% variansi**.

    Akurasi Logistic Regression sebelum PCA adalah
    **{acc_before:.4f}**, sedangkan setelah PCA adalah
    **{acc:.4f}**.

    Preprocessing dan PCA hanya di-fit pada data training,
    kemudian diterapkan pada data testing. Dengan demikian,
    proses mengikuti prinsip anti-data leakage.
    """
)
