
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "models" / "svm_titanic.joblib"

st.title("🚢 Prediksi Keselamatan Penumpang")

st.write("""
Masukkan karakteristik penumpang untuk memprediksi
apakah penumpang diperkirakan selamat atau tidak
menggunakan algoritma Support Vector Machine.
""")

if not MODEL_PATH.exists():
    st.error("Model belum tersedia. Jalankan svm_model.py terlebih dahulu.")
    st.stop()

model = joblib.load(MODEL_PATH)

st.divider()

st.subheader("Input Data Penumpang")

with st.form("form_prediksi"):

    col1, col2 = st.columns(2)

    with col1:

        pclass = st.selectbox(
            "Kelas Tiket",
            [1, 2, 3]
        )

        sex = st.selectbox(
            "Jenis Kelamin",
            ["male", "female"],
            format_func=lambda x: "Laki-laki" if x == "male" else "Perempuan"
        )

        age = st.number_input(
            "Usia Penumpang",
            min_value=0,
            max_value=100,
            value=25,
            step=1
        )

        sibsp = st.number_input(
            "Jumlah Saudara/Pasangan",
            min_value=0,
            max_value=10,
            value=0,
            step=1
        )

    with col2:

        parch = st.number_input(
            "Jumlah Orang Tua/Anak",
            min_value=0,
            max_value=10,
            value=0,
            step=1
        )

        fare = st.number_input(
            "Harga Tiket",
            min_value=0.0,
            value=30.0,
            step=1.0
        )

        embarked = st.selectbox(
            "Pelabuhan Keberangkatan",
            ["S", "C", "Q"],
            format_func=lambda x: {
                "S": "Southampton",
                "C": "Cherbourg",
                "Q": "Queenstown"
            }[x]
        )

    submit = st.form_submit_button(
        "Prediksi Sekarang",
        type="primary",
        use_container_width=True
    )

if submit:

    input_data = pd.DataFrame([{
        "Pclass": pclass,
        "Sex": sex,
        "Age": age,
        "SibSp": sibsp,
        "Parch": parch,
        "Fare": fare,
        "Embarked": embarked
    }])

    hasil = model.predict(input_data)[0]

    st.divider()

    st.subheader("Hasil Prediksi")

    if hasil == 1:
        st.success("Penumpang diprediksi SELAMAT.")
    else:
        st.error("Penumpang diprediksi TIDAK SELAMAT.")

    st.subheader("Data yang Dimasukkan")

    st.dataframe(
        input_data,
        use_container_width=True
    )

    st.caption(
        "Hasil merupakan prediksi model machine learning, "
        "bukan kepastian kondisi sebenarnya."
    )
