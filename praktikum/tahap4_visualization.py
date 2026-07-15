import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import plot_tree
from sklearn.ensemble import RandomForestClassifier

def tampilkan(df, model, fitur):
    st.title("Tahap 4: Visualisasi Hasil Klasifikasi")
    
    st.subheader("1. Aturan Pohon Keputusan (Decision Logic)")
    fig, ax = plt.subplots(figsize=(14, 6))
    
    # PENYESUAIAN ALGORITMA: Pengecekan jenis model agar tidak error saat menggambar
    if isinstance(model, RandomForestClassifier):
        st.info("💡 **Catatan:** Karena Anda menggunakan algoritma **Random Forest** (Ensemble), diagram di bawah ini hanya menampilkan **salah satu pohon perwakilan (Pohon ke-0)** dari ratusan pohon yang bekerja sama di dalam mesin.")
        # Mengambil satu pohon saja dari sekian banyak pohon di Random Forest
        pohon_visual = model.estimators_[0]
    else:
        # Jika menggunakan Decision Tree biasa
        pohon_visual = model

    plot_tree(pohon_visual, 
              feature_names=fitur, 
              class_names=model.classes_, 
              filled=True, 
              rounded=True,
              fontsize=10,
              ax=ax)
    st.pyplot(fig)

    st.subheader("2. Peta Persebaran Performa Negara")
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    warna_kustom = {"Kritis": "#e74c3c", "Menengah": "#f1c40f", "Sangat Baik": "#2ecc71"}

    sns.scatterplot(
        data=df, 
        x='Recovered / 100 Cases', 
        y='Deaths / 100 Cases', 
        hue='Status_Performa',
        palette=warna_kustom,
        size='Active',
        sizes=(30, 600),
        alpha=0.8,
        ax=ax2
    )
    plt.title("Tingkat Kematian vs Kesembuhan (Berdasarkan Target)")
    plt.grid(True, linestyle='--', alpha=0.5)
    st.pyplot(fig2)

    st.subheader("3. Tabel Final Klasifikasi")
    kolom_tampil = ['Country/Region', 'Status_Performa', 'Recovered / 100 Cases', 'Deaths / 100 Cases']
    st.dataframe(df[kolom_tampil].style.applymap(
        lambda val: 'background-color: #ffcccc' if val == 'Kritis' else ('background-color: #ccffcc' if val == 'Sangat Baik' else ''),
        subset=['Status_Performa']
    ), use_container_width=True)