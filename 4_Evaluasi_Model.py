
import streamlit as st
import pandas as pd
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents
RESULT_PATH = ROOT / "models" / "evaluation.json"

st.title("📈 Evaluasi Model SVM")

st.write("""
Evaluasi dilakukan untuk mengetahui kemampuan model
SVM dalam mengklasifikasikan keselamatan penumpang Titanic.
""")

if not RESULT_PATH.exists():

    st.warning("Hasil evaluasi belum tersedia. Jalankan svm_model.py.")
    st.stop()

with open(RESULT_PATH, "r") as file:
    result = json.load(file)

# Metrik evaluasi
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    st.metric(
        "Accuracy",
        f"{result['accuracy'] * 100:.2f}%"
    )

with col2:
    st.metric(
        "Precision",
        f"{result['precision'] * 100:.2f}%"
    )

with col3:
    st.metric(
        "Recall",
        f"{result['recall'] * 100:.2f}%"
    )

with col4:
    st.metric(
        "F1-Score",
        f"{result['f1_score'] * 100:.2f}%"
    )

st.divider()

st.subheader("Pembagian Dataset")

st.write("Data training:", result["train_size"])
st.write("Data testing:", result["test_size"])

st.divider()

st.subheader("Confusion Matrix")

cm = result["confusion_matrix"]

cm_df = pd.DataFrame(
    cm,
    index=["Aktual Tidak Selamat", "Aktual Selamat"],
    columns=["Prediksi Tidak Selamat", "Prediksi Selamat"]
)

st.dataframe(
    cm_df,
    use_container_width=True
)

st.subheader("Visualisasi Confusion Matrix")

st.bar_chart(cm_df)

st.divider()

st.subheader("Classification Report")

report = pd.DataFrame(
    result["classification_report"]
).transpose()

st.dataframe(
    report,
    use_container_width=True
)
