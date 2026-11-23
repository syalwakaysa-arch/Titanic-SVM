
# ==========================
# CUSTOM CSS
# ==========================

st.markdown("""
<style>

/* BACKGROUND UTAMA */
.stApp {
    background-color: #F4F7FC;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #142D4E, #1E4775);
}

/* TULISAN SIDEBAR */
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] label {
    color: #FFFFFF;
}

/* JUDUL GRUP SIDEBAR */
section[data-testid="stSidebar"] [data-testid="stSidebarNav"] span {
    color: #EAF2FF;
}

/* MENU NAVIGASI */
section[data-testid="stSidebar"]
[data-testid="stSidebarNav"] a {
    border-radius: 10px;
    margin: 5px 8px;
    padding: 10px 12px;
    transition: 0.3s;
}

/* MENU AKTIF */
section[data-testid="stSidebar"]
[data-testid="stSidebarNav"] a[aria-current="page"] {
    background-color: #3B82C4;
    border-left: 4px solid #FFFFFF;
}

/* HOVER MENU */
section[data-testid="stSidebar"]
[data-testid="stSidebarNav"] a:hover {
    background-color: #315D8D;
}

/* JUDUL UTAMA */
h1 {
    color: #163A63;
    font-weight: 800;
}

h2, h3 {
    color: #245580;
}

/* PARAGRAF */
p {
    color: #334155;
}

/* KARTU METRIK */
[data-testid="stMetric"] {
    background-color: #FFFFFF;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #DCE6F2;
    box-shadow: 0 2px 8px rgba(20, 45, 78, 0.06);
}

/* TOMBOL */
.stButton > button {
    background-color: #2563A6;
    color: white;
    border-radius: 9px;
    border: none;
    padding: 8px 20px;
    font-weight: 600;
}

/* HOVER TOMBOL */
.stButton > button:hover {
    background-color: #163A63;
    color: white;
    border: none;
}

/* INPUT */
.stTextInput input,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"] {
    border-radius: 8px;
}

/* CONTAINER */
[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 12px;
}

/* KONTEN UTAMA */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* PEMBATAS */
hr {
    border-color: #DCE6F2;
}

</style>
""", unsafe_allow_html=True)
