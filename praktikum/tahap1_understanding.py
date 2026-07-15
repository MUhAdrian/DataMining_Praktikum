import streamlit as st

def tampilkan(df):
    st.title("Tahap 1: Data Understanding")
    st.markdown("Mengeksplorasi dataset mentah sebelum algoritma diterapkan untuk memahami struktur dasarnya.")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Negara (Baris)", df.shape[0])
    col2.metric("Total Atribut (Kolom)", df.shape[1])
    col3.metric("Data Kosong (Missing Values)", df.isnull().sum().sum())
    
    st.subheader("Sampel Data Mentah")
    st.dataframe(df.head(10), use_container_width=True)
    
    st.subheader("Statistik Deskriptif")
    st.markdown("Melihat nilai rata-rata, minimal, dan maksimal dari fitur utama.")
    st.dataframe(df[['Confirmed', 'Deaths', 'Recovered', 'Active']].describe(), use_container_width=True)