
import streamlit as st

st.set_page_config(
    page_title="Titanic SVM Prediction",
    page_icon="🚢",
    layout="wide"
)

# ==============================
# PENGANTAR
# ==============================

beranda = st.Page(
    "0_Beranda.py",
    title="Beranda",
    icon="🏠",
    url_path="beranda",
    default=True,
)

dataset = st.Page(
    "1_Dataset.py",
    title="Tentang Dataset",
    icon="🗃️",
    url_path="dataset"
)

eda = st.Page(
    "7_Eksplorasi_Data.py",
    title="Eksplorasi Data (EDA)",
    icon="📊",
    url_path="eksplorasi-data"
)

# ==============================
# PENGOLAHAN & MODEL
# ==============================

pembersihan = st.Page(
    "2_Pembersihan_Data.py",
    title="Pembersihan Data",
    icon="🎚️",
    url_path="pembersihan-data"
)

model = st.Page(
    "3_Model_SVM.py",
    title="Model SVM",
    icon="🧠",
    url_path="model-svm"
)

evaluasi = st.Page(
    "4_Evaluasi_Model.py",
    title="Evaluasi Model",
    icon="📈",
    url_path="evaluasi-model"
)

# ==============================
# PENERAPAN
# ==============================

prediksi = st.Page(
    "5_Prediksi.py",
    title="Prediksi Penumpang",
    icon="🚢",
    url_path="prediksi"
)

# ==============================
# LAINNYA
# ==============================

tentang = st.Page(
    "6_Tentang.py",
    title="Tentang Aplikasi",
    icon="ℹ️",
    url_path="tentang"
)

# ==============================
# NAVIGASI UTAMA
# ==============================

pg = st.navigation({
    "PENGANTAR": [
        beranda,
        dataset,
        eda
    ],

    "PENGOLAHAN & MODEL": [
        pembersihan,
        model,
        evaluasi
    ],

    "PENERAPAN": [
        prediksi
    ],

    "LAINNYA": [
        tentang
    ]
})

pg.run()
