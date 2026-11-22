
import streamlit as st
import joblib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MODEL_PATH = ROOT / "models" / "svm_titanic.joblib"

st.title("🧠 Model Support Vector Machine")

st.write("""
Halaman ini menjelaskan model Support Vector Machine
yang digunakan untuk klasifikasi keselamatan penumpang.
""")

st.subheader("Konsep Support Vector Machine")

st.write("""
Support Vector Machine merupakan algoritma machine learning
yang digunakan untuk klasifikasi dengan mencari hyperplane
terbaik untuk memisahkan kelas data.

Dalam penelitian ini, SVM digunakan untuk mengklasifikasikan
penumpang Titanic ke dalam dua kelas, yaitu selamat dan
tidak selamat.
""")

st.divider()

st.subheader("Konfigurasi Model")

st.write("Algoritma: Support Vector Classifier (SVC)")
st.write("Kernel: Radial Basis Function (RBF)")
st.write("Parameter C: 1.0")
st.write("Gamma: scale")

st.divider()

st.subheader("Status Model")

if MODEL_PATH.exists():

    model = joblib.load(MODEL_PATH)

    st.success("Model SVM berhasil dimuat.")

    st.write("Jenis model:", type(model).__name__)

else:

    st.warning(
        "Model belum ditemukan. Jalankan svm_model.py terlebih dahulu."
    )

st.divider()

st.subheader("Tahapan Pembuatan Model")

st.write("""
1. Menyiapkan dataset.
2. Memisahkan fitur dan target.
3. Membagi data training dan testing.
4. Melakukan preprocessing.
5. Membuat model SVM.
6. Melatih model menggunakan data training.
7. Menyimpan model menggunakan Joblib.
""")
