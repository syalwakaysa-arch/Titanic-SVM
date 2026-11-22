
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

ROOT = Path(__file__).resolve().parents

st.title("📊 Eksplorasi Data Titanic")

st.write("""
Halaman ini digunakan untuk mengeksplorasi karakteristik
penumpang Titanic sebelum dilakukan proses pemodelan
menggunakan algoritma Support Vector Machine.
""")

@st.cache_data
def load_data():
    return pd.read_csv(ROOT / "titanic.csv")

df = load_data()

st.divider()

st.subheader("1. Informasi Dataset")

col1, col2, col3 = st.columns(3)

col1.metric("Jumlah Penumpang", df.shape[0])
col2.metric("Jumlah Fitur", df.shape[1])
col3.metric("Missing Values", int(df.isnull().sum().sum()))

st.divider()

st.subheader("2. Distribusi Keselamatan Penumpang")

jumlah = df["Survived"].value_counts().sort_index()

grafik = pd.DataFrame({
    "Status": ["Tidak Selamat", "Selamat"],
    "Jumlah": [
        jumlah.get(0, 0),
        jumlah.get(1, 0)
    ]
})

st.bar_chart(
    grafik.set_index("Status")
)

st.divider()

st.subheader("3. Distribusi Jenis Kelamin")

st.bar_chart(df["Sex"].value_counts())

st.divider()

st.subheader("4. Distribusi Kelas Penumpang")

st.bar_chart(df["Pclass"].value_counts().sort_index())

st.divider()

st.subheader("5. Statistik Deskriptif")

st.dataframe(
    df.describe(),
    use_container_width=True
)

st.divider()

st.subheader("6. Korelasi Antar Fitur Numerik")

numerik = df.select_dtypes(include="number")

fig, ax = plt.subplots(figsize=(10, 6))

im = ax.imshow(numerik.corr(), cmap="coolwarm")

ax.set_xticks(range(len(numerik.columns)))
ax.set_yticks(range(len(numerik.columns)))

ax.set_xticklabels(numerik.columns, rotation=45, ha="right")
ax.set_yticklabels(numerik.columns)

fig.colorbar(im, ax=ax)

st.pyplot(fig)
plt.close(fig)
