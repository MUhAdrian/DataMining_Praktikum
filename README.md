# DataMining_Praktikum
Dashboard Klasifikasi Performa Penanganan COVID-19 Global

Aplikasi berbasis web (web-dashboard) interaktif yang memanfaatkan Machine Learning untuk mengklasifikasikan tingkat keberhasilan penanganan pandemi COVID-19 di 187 negara.

Proyek ini dibangun menggunakan Python dan Streamlit, dengan mengimplementasikan algoritma Decision Tree dan Random Forest untuk mengelompokkan negara ke dalam 3 kategori performa: Sangat Baik, Menengah, dan Kritis.

Deskripsi Proyek

Bagaimana kita bisa menilai apakah suatu negara berhasil atau kewalahan dalam menangani pandemi? Menggunakan metrik absolut (seperti total jumlah kasus) seringkali bias terhadap negara berpopulasi besar.

Proyek ini memecahkan masalah tersebut dengan melakukan Feature Engineering—mengubah data mentah menjadi rasio proporsional—lalu melatih model Machine Learning untuk menemukan batas logis kedaruratan suatu wilayah tanpa mengalami kebocoran data (Data Leakage).

Sistem ini disusun menggunakan arsitektur multi-file yang mensimulasikan alur kerja CRISP-DM (Data Understanding -> Preprocessing -> Modeling -> Visualization), menjadikannya sangat modular dan mudah dikembangkan secara ilmiah.

Fitur Utama

Data Understanding: Pratinjau data mentah metrik COVID-19 dari 187 negara beserta statistik deskriptifnya.

Preprocessing Transparan: Sistem memperlihatkan secara langsung aturan rekayasa fitur (labeling) untuk target klasifikasi.

Modeling Interaktif: Pengguna dapat memilih algoritma (Decision Tree / Random Forest) dan mengatur hyperparameter (seperti Max Depth dan n_estimators) secara real-time via sidebar.

Visualisasi Prediksi: Menampilkan grafik evaluasi Confusion Matrix, Scatter Plot pemetaan negara, dan render visual diagram Pohon Keputusan (Decision Logic).

Teknologi yang Digunakan

Bahasa Pemrograman: Python 3.x

Front-end / Antarmuka: Streamlit

Machine Learning: Scikit-Learn (Decision Tree, Random Forest)

Manipulasi Data: Pandas, NumPy

Visualisasi Data: Matplotlib, Seaborn

Cara Menjalankan Aplikasi (Lokal)

Clone repositori ini:

git clone https://github.com/username-anda/nama-repo-ini.git
cd nama-repo-ini


Install library yang dibutuhkan:

pip install streamlit pandas numpy scikit-learn matplotlib seaborn


Jalankan server Streamlit:

streamlit run app.py


Aplikasi akan otomatis terbuka di browser melalui http://localhost:8501.

Pengembang

Proyek analisis dan pengembangan sistem pendukung keputusan ini dikembangkan secara kolaboratif oleh:

Iqbal Al Anshori

Wasis Wibisono

M. Adrian A.F

Dibuat untuk pemenuhan tugas riset praktikum Data Mining dan Machine Learning.
