import streamlit as st
import pandas as pd

# Mengimpor modul/file proses yang akan kita buat
import tahap1_understanding
import tahap2_preprocessing
import tahap3_modeling_eval
import tahap4_visualization

st.set_page_config(page_title="Dashboard COVID-19", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("country_wise_latest.csv")

# Memuat data mentah
df_raw = load_data()

# Menjalankan preprocessing di latar belakang agar data siap digunakan oleh semua menu
df_processed, fitur_awal = tahap2_preprocessing.proses_data(df_raw.copy())

# Membuat Navigasi Sidebar
st.sidebar.title("Tahapan Proses CRISP-DM")
menu = st.sidebar.radio(
    "Pilih Modul:",
    ("1. Data Understanding", "2. Preprocessing Data", "3. Modeling & Evaluasi", "4. Visualisasi Hasil")
)

st.sidebar.markdown("---")
st.sidebar.info("Aplikasi ini dibangun dengan struktur modular (Multi-file).")

# Router/Controller Logika Navigasi
if menu == "1. Data Understanding":
    tahap1_understanding.tampilkan(df_raw)

elif menu == "2. Preprocessing Data":
    tahap2_preprocessing.tampilkan(df_raw, df_processed)

elif menu == "3. Modeling & Evaluasi":
    # Menangkap 4 variabel dari tahap 3 (termasuk fitur_optimal yang sudah diperbarui)
    model_terlatih, X, y, fitur_optimal = tahap3_modeling_eval.tampilkan(df_processed, fitur_awal)
    
    # Menyimpan model dan fitur ke session_state
    st.session_state['model'] = model_terlatih
    st.session_state['fitur_optimal'] = fitur_optimal

elif menu == "4. Visualisasi Hasil":
    # Mengecek apakah model dan fitur_optimal sudah tersimpan di memori Streamlit
    if 'model' not in st.session_state or 'fitur_optimal' not in st.session_state:
        st.warning("⚠️ Silakan buka menu '3. Modeling & Evaluasi' terlebih dahulu untuk melatih algoritma.")
    else:
        # Mengirimkan data dan model ke tahap 4
        tahap4_visualization.tampilkan(df_processed, st.session_state['model'], st.session_state['fitur_optimal'])