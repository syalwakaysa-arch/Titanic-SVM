
import streamlit as st
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents

st.title("🧹 Pembersihan Data")

st.write("""
Tahap pembersihan data dilakukan untuk memastikan
dataset siap digunakan dalam proses pelatihan model SVM.
""")

df = pd.read_csv(ROOT / "titanic.csv")

st.subheader("1. Pemeriksaan Missing Values")

missing = pd.DataFrame({
    "Kolom": df.columns,
    "Jumlah Data Kosong": df.isnull().sum().values,
    "Persentase (%)": (
        df.isnull().mean().values * 100
    ).round(2)
})

st.dataframe(
    missing,
    use_container_width=True,
    hide_index=True
)

st.subheader("Visualisasi Missing Values")

st.bar_chart(
    missing.set_index("Kolom")["Jumlah Data Kosong"]
)

st.divider()

st.subheader("2. Penanganan Missing Values")

st.write("""
Penanganan nilai kosong dilakukan dengan metode:

- Data numerik: menggunakan median.
- Data kategorik: menggunakan modus.
- Data target Survived yang kosong: baris dihapus.
""")

st.divider()

st.subheader("3. Transformasi Data")

st.write("""
Transformasi data dilakukan melalui beberapa proses:

1. StandardScaler digunakan untuk standardisasi data numerik.
2. OneHotEncoder digunakan untuk mengubah data kategorik menjadi bentuk numerik.
3. ColumnTransformer digunakan untuk menggabungkan proses preprocessing.
4. Pipeline mengintegrasikan preprocessing dengan model SVM.
""")

st.info("""
Seluruh proses preprocessing untuk pelatihan model
dijalankan secara otomatis melalui Pipeline pada svm_model.py.
""")
