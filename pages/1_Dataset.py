import streamlit as st
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parent

st.title("📊 Dataset Titanic")

st.write("""
Halaman ini menampilkan dataset Titanic yang digunakan
dalam implementasi algoritma Support Vector Machine.
""")


@st.cache_data
def load_data():
    return pd.read_csv(ROOT / "titanic.csv")


df = load_data()

# Informasi dataset
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Data", df.shape[0])

with col2:
    st.metric("Total Kolom", df.shape[1])

with col3:
    st.metric("Data Duplikat", int(df.duplicated().sum()))

st.divider()

st.subheader("Data Penumpang Titanic")

st.dataframe(df, width="stretch", hide_index=True)

st.divider()

st.subheader("Informasi Dataset")

info = pd.DataFrame({
    "Nama Kolom": df.columns,
    "Tipe Data": df.dtypes.astype(str).values,
    "Data Kosong": df.isnull().sum().values,
})

st.dataframe(info, width="stretch", hide_index=True)

st.divider()

st.subheader("Statistik Deskriptif")

st.dataframe(df.describe(), width="stretch")

st.divider()

st.subheader("Distribusi Keselamatan Penumpang")

jumlah = df["Survived"].value_counts().sort_index()

grafik = pd.DataFrame({
    "Status": ["Tidak Selamat", "Selamat"],
    "Jumlah": [jumlah.get(0, 0), jumlah.get(1, 0)],
})

st.bar_chart(grafik.set_index("Status"))
