import streamlit as st

# Logika inti untuk membuat target
def tentukan_status(row):
    if row['Deaths / 100 Cases'] > 4.0:
        return "Kritis"
    elif row['Recovered / 100 Cases'] >= 75.0 and row['Deaths / 100 Cases'] <= 3.0:
        return "Sangat Baik"
    else:
        return "Menengah"

# Fungsi ini dijalankan oleh app.py di latar belakang
def proses_data(df):
    df['Status_Performa'] = df.apply(tentukan_status, axis=1)
    fitur = ['Recovered / 100 Cases', 'Deaths / 100 Cases', 'Active', 'New cases']
    return df, fitur

# Fungsi antarmuka visual
def tampilkan(df_raw, df_processed):
    st.title("Tahap 2: Preprocessing & Rekayasa Fitur")
    st.markdown("""
    Pada tahap ini, kita merekayasa fitur baru bernama **Status_Performa**. 
    Karena algoritma *Decision Tree* adalah *Supervised Learning*, ia membutuhkan target untuk dipelajari.
    """)
    
    st.subheader("Aturan Logika Pembuatan Target (Labeling)")
    st.code("""
    JIKA Tingkat Kematian > 4.0 MAKA "Kritis"
    JIKA Tingkat Kesembuhan >= 75.0 DAN Kematian <= 3.0 MAKA "Sangat Baik"
    LAINNYA MAKA "Menengah"
    """, language="python")
    
    st.subheader("Hasil Preprocessing")
    st.markdown("Perhatikan kolom paling kanan yang telah ditambahkan sistem:")
    st.dataframe(df_processed[['Country/Region', 'Recovered / 100 Cases', 'Deaths / 100 Cases', 'Status_Performa']].head(10), use_container_width=True)