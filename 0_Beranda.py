
import streamlit as st

st.title("🚢 Titanic Survival Prediction")

st.subheader(
    "Implementasi Algoritma Support Vector Machine (SVM)"
)

st.write("""
Selamat datang di aplikasi Titanic Survival Prediction.

Aplikasi ini merupakan implementasi algoritma Support Vector
Machine untuk melakukan klasifikasi dan memprediksi keselamatan
penumpang kapal Titanic berdasarkan karakteristik penumpang.
""")

st.divider()

st.header("Tentang Aplikasi")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Dataset", "Titanic")

with col2:
    st.metric("Algoritma", "SVM")

with col3:
    st.metric("Jenis Sistem", "Klasifikasi")

st.divider()

st.header("Fitur Aplikasi")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 📊 Dataset
    Menampilkan data penumpang Titanic.

    ### 🧹 Pembersihan Data
    Menampilkan proses penanganan missing values,
    encoding, dan standardisasi.
    """)

with col2:
    st.markdown("""
    ### 🧠 Model SVM
    Menampilkan informasi algoritma SVM.

    ### 📈 Evaluasi Model
    Menampilkan hasil pengujian model.

    ### 🚢 Prediksi
    Melakukan prediksi keselamatan penumpang.
    """)

st.divider()

st.info(
    "Silakan pilih halaman melalui menu navigasi di sebelah kiri."
)

st.caption(
    "Titanic Survival Prediction | Machine Learning Project"
)
