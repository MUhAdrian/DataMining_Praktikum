import streamlit as st
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score, 
    confusion_matrix, classification_report
)

def tampilkan(df, fitur_awal):
    st.title("Tahap 3: Modeling & Evaluasi")
    
    df['Deaths / 100 Recovered'] = df['Deaths / 100 Recovered'].replace([np.inf, -np.inf], 0)
    
    fitur_optimal = ['Deaths / 100 Recovered', '1 week % increase', 'New cases', 'New deaths', 'Active']
    X = df[fitur_optimal]
    y = df['Status_Performa']
    
    # 2. TRAIN-TEST SPLIT
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # 3. KONTROL SIDEBAR
    st.sidebar.markdown("---")
    st.sidebar.subheader("Penyesuaian Algoritma")
    pilihan_algo = st.sidebar.radio(
        "Pilih Algoritma Klasifikasi:",
        ("Decision Tree (Single)", "Random Forest (Ensemble)")
    )
    
    # 4. INSTANSIASI MODEL BERDASARKAN PILIHAN
    if pilihan_algo == "Decision Tree (Single)":
        max_depth = st.sidebar.slider("Hyperparameter: Max Depth", min_value=2, max_value=10, value=5)
        model = DecisionTreeClassifier(max_depth=max_depth, random_state=42)
    else:
        n_estimators = st.sidebar.slider("Jumlah Pohon (n_estimators)", min_value=50, max_value=200, value=100)
        max_depth = st.sidebar.slider("Maksimal Kedalaman", min_value=2, max_value=10, value=5)
        model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
    
    # 5. PELATIHAN & PREDIKSI
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    # 6. KALKULASI METRIK
    akurasi = accuracy_score(y_test, y_pred)
    presisi = precision_score(y_test, y_pred, average='weighted', zero_division=0)
    recall = recall_score(y_test, y_pred, average='weighted', zero_division=0)
    f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)
    
    cm = confusion_matrix(y_test, y_pred)
    report = classification_report(y_test, y_pred, zero_division=0)
    
    # 7. TAMPILAN ANTARMUKA EVALUASI
    st.success(f"Berhasil melatih model menggunakan **{pilihan_algo}** dengan fitur yang telah dioptimasi.")
    
    st.subheader(f"A. EVALUASI ALGORITMA ({pilihan_algo.upper()})")
    
    st.markdown("**1. Confusion Matrix (Numerik):**")
    st.code(cm, language='plaintext')
    
    st.markdown("**2. Metrik Performa (Data Testing):**")
    st.code(f"""
- Accuracy  : {akurasi:.4f}
- Precision : {presisi:.4f}
- Recall    : {recall:.4f}
- F1-Score  : {f1:.4f}
    """, language='plaintext')
    
    st.markdown("**Laporan Klasifikasi Lengkap:**")
    st.code(report, language='plaintext')
    
    return model, X, y, fitur_optimal