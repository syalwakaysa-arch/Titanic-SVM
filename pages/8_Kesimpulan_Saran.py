
import streamlit as st

st.set_page_config(
    page_title="Kesimpulan dan Saran",
    page_icon="🚢",
    layout="wide"
)

st.title("Kesimpulan dan Saran")
st.write(
    "Ringkasan hasil penerapan algoritma Machine Learning "
    "untuk klasifikasi keselamatan penumpang Titanic."
)

st.markdown("---")


# ==========================
# 1. KESIMPULAN
# ==========================

st.header("1. Kesimpulan")

st.markdown("""
Berdasarkan proses analisis dan penerapan Machine Learning pada
dataset Titanic, dapat disimpulkan beberapa hal berikut.

**1. Karakteristik Dataset**

Dataset Titanic terdiri dari 891 data penumpang dengan target
klasifikasi biner, yaitu `Survived` (0 = tidak selamat dan
1 = selamat). Dataset memiliki fitur numerik dan kategorikal,
nilai hilang, serta perbedaan skala antarfitur.

Distribusi target terdiri dari 549 penumpang tidak selamat
dan 342 penumpang selamat. Kondisi ini menunjukkan
ketidakseimbangan kelas yang relatif ringan.

**2. Preprocessing Data**

Tahap preprocessing dilakukan dengan menghapus fitur yang
tidak relevan, yaitu `PassengerId`, `Name`, `Ticket`, dan `Cabin`.
Nilai hilang pada `Age` ditangani menggunakan median,
sedangkan `Embarked` menggunakan modus.

Fitur numerik diproses menggunakan `StandardScaler`,
sementara fitur kategorikal diproses menggunakan
`OneHotEncoder`.

Pembagian data dilakukan secara stratified dengan rasio
80:20 sebelum preprocessing untuk mencegah data leakage.

**3. Penerapan Algoritma Machine Learning**

Enam algoritma diterapkan untuk menyelesaikan permasalahan
klasifikasi Titanic, yaitu:

- Logistic Regression (L2)
- K-Nearest Neighbors (K-NN)
- Support Vector Classifier (SVC) dengan kernel RBF
- Decision Tree
- Random Forest
- HistGradientBoosting

Algoritma tersebut memiliki karakteristik yang berbeda,
sehingga dapat dibandingkan untuk mengetahui pendekatan
yang paling sesuai dengan dataset Titanic.

**4. Evaluasi Model**

Evaluasi model dilakukan menggunakan Stratified 5-Fold
Cross-Validation pada data latih. Pemilihan model didasarkan
pada nilai F1-score tertinggi.

Setelah model terbaik ditentukan, evaluasi akhir dilakukan
satu kali menggunakan data uji. Metrik yang digunakan meliputi
Accuracy, Precision, Recall, F1-score, dan ROC-AUC.

**5. Deployment**

Model terpilih dilatih kembali menggunakan seluruh dataset
setelah proses seleksi selesai. Pipeline disimpan menggunakan
Joblib sehingga preprocessing dan model dapat digunakan
secara bersamaan untuk memprediksi data penumpang baru.

**6. Reduksi Dimensi**

Berdasarkan audit karakteristik dataset, jumlah sampel
sebanyak 891 dengan sekitar 7 fitur efektif setelah kurasi.
Oleh karena itu, PCA tidak menjadi kebutuhan utama dalam
pemodelan berdasarkan rasio jumlah sampel terhadap fitur.

Namun, PCA tetap dapat digunakan sebagai eksperimen
reduksi dimensi untuk mempelajari pengaruh jumlah fitur
terhadap variansi dan performa model.
""")


st.markdown("---")


# ==========================
# 2. SARAN
# ==========================

st.header("2. Saran")

st.markdown("""
Berdasarkan hasil analisis dan keterbatasan penelitian,
terdapat beberapa saran untuk pengembangan selanjutnya.

**1. Pengembangan Fitur (Feature Engineering)**

Penelitian selanjutnya dapat menambahkan fitur baru seperti
`FamilySize` yang menggabungkan informasi `SibSp` dan `Parch`.
Selain itu, gelar penumpang dapat diekstraksi dari kolom `Name`
sebelum kolom tersebut dihapus.

**2. Optimasi Hyperparameter**

Optimasi parameter model dapat dilakukan menggunakan
`GridSearchCV` atau `RandomizedSearchCV` untuk memperoleh
kombinasi parameter yang lebih optimal, khususnya pada
algoritma SVM dengan kernel RBF.

**3. Pengembangan Evaluasi Model**

Evaluasi sebaiknya tidak hanya berfokus pada accuracy,
tetapi juga mempertimbangkan Precision, Recall, F1-score,
dan ROC-AUC agar kemampuan klasifikasi setiap model
dapat dianalisis secara lebih menyeluruh.

**4. Validasi Berbasis Kelompok**

Penumpang yang memiliki hubungan keluarga atau nomor tiket
yang sama berpotensi saling berkaitan. Penelitian berikutnya
dapat mempertimbangkan validasi berbasis kelompok seperti
`StratifiedGroupKFold` agar evaluasi lebih memperhatikan
struktur hubungan antarpenumpang.

**5. Pengembangan Model SVM**

Pengembangan berikutnya dapat menguji berbagai nilai
`C`, `gamma`, dan kernel SVM untuk mendapatkan konfigurasi
yang memberikan performa klasifikasi lebih baik.

**6. Pengembangan Aplikasi**

Aplikasi dapat dikembangkan dengan menambahkan visualisasi
hasil evaluasi, penyimpanan model, serta fitur prediksi
penumpang baru yang lebih interaktif dan informatif.

**7. Eksperimen Reduksi Dimensi**

PCA dapat dikaji lebih lanjut untuk membandingkan jumlah
komponen utama, variansi yang dipertahankan, serta pengaruhnya
terhadap performa model klasifikasi.
""")


st.markdown("---")


# ==========================
# 3. PENUTUP
# ==========================

st.header("3. Penutup")

st.success("""
Penerapan Machine Learning pada dataset Titanic menunjukkan
bahwa proses pemilihan algoritma perlu disesuaikan dengan
karakteristik data, strategi preprocessing, dan metode evaluasi.

Melalui tahapan CRISP-DM, penelitian ini diharapkan dapat
menghasilkan proses klasifikasi yang sistematis, terukur,
dan dapat dikembangkan lebih lanjut.
""")

st.caption(
    "Proyek Klasifikasi Keselamatan Penumpang Titanic — Kelompok 8"
)
