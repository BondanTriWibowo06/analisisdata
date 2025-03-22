# Proyek Analisis Data: Bike Sharing Dataset dengan Streamlit

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df_day = pd.read_csv("day.csv")
df_hour = pd.read_csv("hour.csv")

def main():
    st.title("Bike Sharing Dashboard")
    st.sidebar.title("Bondan Tri Wibowo bondan.tri@lintasarta.co.id L000YWL027")
    st.sidebar.title("Navigasi")
    menu = st.sidebar.selectbox("Pilih Analisis", [
        "Overview Data",
        "Analisis Peminjaman Sepeda",
        "Faktor yang Mempengaruhi",
        "Clustering Binning",
        "Time Series Analysis",
    ])

    if menu == "Overview Data":
        st.subheader("Preview Dataset")
        st.write("### Data Harian")
        st.dataframe(df_day.head())
        st.write("### Data Jam")
        st.dataframe(df_hour.head())


    elif menu == "Analisis Peminjaman Sepeda":
        st.subheader("Distribusi Peminjaman Sepeda")
        fig, ax = plt.subplots(figsize=(8,5))
        sns.histplot(df_day['cnt'], bins=30, kde=True, color='blue', ax=ax)
        ax.set_xlabel("Jumlah Peminjaman Sepeda")
        ax.set_ylabel("Frekuensi")
        ax.set_title("Distribusi Peminjaman Sepeda Harian")
        st.pyplot(fig)

    elif menu == "Faktor yang Mempengaruhi":
        st.subheader("Korelasi Variabel")
        
        # Hanya pilih kolom numerik untuk menghindari error
        df_corr = df_day.select_dtypes(include=[np.number])

        fig, ax = plt.subplots(figsize=(10,6))
        sns.heatmap(df_corr.corr(), annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
        ax.set_title("Matriks Korelasi Antar Variabel")
        st.pyplot(fig)

    elif menu == "Clustering Binning":
        st.subheader("Kategori Peminjaman Sepeda")
        bins = [0, 2000, 4000, 6000, 10000]
        labels = ['Rendah', 'Sedang', 'Tinggi', 'Sangat Tinggi']
        df_day['kategori_peminjaman'] = pd.cut(df_day['cnt'], bins=bins, labels=labels)

        fig, ax = plt.subplots(figsize=(8,5))
        sns.countplot(x='kategori_peminjaman', data=df_day, palette='pastel', ax=ax)
        ax.set_xlabel("Kategori Peminjaman")
        ax.set_ylabel("Jumlah Hari")
        ax.set_title("Distribusi Kategori Peminjaman Sepeda")
        st.pyplot(fig)

    elif menu == "Time Series Analysis":
        st.subheader("Tren Peminjaman Sepeda")
        fig, ax = plt.subplots(figsize=(12,6))
        sns.lineplot(x='dteday', y='cnt', data=df_day, color='blue', ax=ax)
        ax.set_xlabel("Tanggal")
        ax.set_ylabel("Jumlah Peminjaman Sepeda")
        ax.set_title("Tren Peminjaman Sepeda dari Waktu ke Waktu")
        st.pyplot(fig)

if __name__ == "__main__":
    main()
