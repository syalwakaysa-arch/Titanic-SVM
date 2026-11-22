import streamlit as st

st.set_page_config(
    page_title="Titanic SVM",
    page_icon="🚢",
    layout="wide",
)

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
    icon="📄",
    url_path="dataset",
)

eda = st.Page(
    "7_Eksplorasi_Data.py",
    title="Eksplorasi Data (EDA)",
    icon="📊",
    url_path="eda",
)

pembersihan = st.Page(
    "2_Pembersihan_Data.py",
    title="Pembersihan Data",
    icon="🧹",
    url_path="pembersihan",
)

model = st.Page(
    "3_Model_SVM.py",
    title="Model SVM",
    icon="🧠",
    url_path="model",
)

evaluasi = st.Page(
    "4_Evaluasi_Model.py",
    title="Evaluasi Model",
    icon="📈",
    url_path="evaluasi",
)

prediksi = st.Page(
    "5_Prediksi.py",
    title="Prediksi Penumpang",
    icon="🚢",
    url_path="prediksi",
)

tentang = st.Page(
    "6_Tentang.py",
    title="Tentang Aplikasi",
    icon="ℹ️",
    url_path="tentang",
)

pg = st.navigation(
    {
        "Pengantar": [beranda, dataset, eda],
        "Pengolahan & Model": [pembersihan, model, evaluasi],
        "Penerapan": [prediksi],
        "Lainnya": [tentang],
    }
)

pg.run()
