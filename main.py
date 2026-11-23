import streamlit as st

st.set_page_config(
    page_title="Titanic SVM Classification",
    page_icon="🚢",
    layout="wide"
)

# ==========================
# CUSTOM CSS SIDEBAR
# ==========================

st.markdown("""
<style>

/* Background sidebar */
section[data-testid="stSidebar"] {
    background-color: #202020;
}

/* Tulisan sidebar */
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span {
    color: #E8E8E8;
}

/* Menu navigasi */
section[data-testid="stSidebar"]
[data-testid="stSidebarNav"] a {
    border-radius: 9px;
    margin: 4px 8px;
    padding: 9px 12px;
}

/* Menu aktif */
section[data-testid="stSidebar"]
[data-testid="stSidebarNav"] a[aria-current="page"] {
    background-color: #454545;
    border-left: 3px solid #FFFFFF;
}

/* Hover */
section[data-testid="stSidebar"]
[data-testid="stSidebarNav"] a:hover {
    background-color: #383838;
}

/* Konten utama */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

</style>
""", unsafe_allow_html=True)


# ==========================
# PENGANTAR
# ==========================

beranda = st.Page(
    "pages/0_Beranda.py",
    title="Beranda",
    icon=":material/home:",
    default=True
)

dataset = st.Page(
    "pages/1_Dataset.py",
    title="Tentang Dataset",
    icon=":material/database:"
)

eda = st.Page(
    "pages/7_Eksplorasi_Data.py",
    title="Eksplorasi Data (EDA)",
    icon=":material/bar_chart:"
)


# ==========================
# PENGOLAHAN & MODEL
# ==========================

preprocessing = st.Page(
    "pages/2_Pembersihan_Data.py",
    title="Preprocessing",
    icon=":material/tune:"
)

pca = st.Page(
    "pages/9_Reduksi_Dimensi_PCA.py",
    title="Reduksi Dimensi (PCA)",
    icon=":material/hub:"
)

optimasi = st.Page(
    "pages/3_Model_SVM.py",
    title="Teknik Optimasi (SVM)",
    icon=":material/auto_fix_high:"
)

evaluasi = st.Page(
    "pages/4_Evaluasi_Model.py",
    title="Modelling & Evaluasi",
    icon=":material/analytics:"
)


# ==========================
# PENERAPAN
# ==========================

prediksi = st.Page(
    "pages/5_Prediksi.py",
    title="Prediksi Penumpang",
    icon=":material/person_search:"
)

kesimpulan = st.Page(
    "pages/8_Kesimpulan_Saran.py",
    title="Kesimpulan & Saran",
    icon=":material/task_alt:"
)


# ==========================
# NAVIGASI UTAMA
# ==========================

pg = st.navigation({

    "Pengantar": [
        beranda,
        dataset,
        eda
    ],

    "Pengolahan & Model": [
        preprocessing,
        pca,
        optimasi,
        evaluasi
    ],

    "Penerapan": [
        prediksi,
        kesimpulan
    ]

})

pg.run()
