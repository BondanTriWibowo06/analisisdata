import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df_day = pd.read_csv("day.csv")

# Konversi kolom tanggal ke format datetime
df_day['dteday'] = pd.to_datetime(df_day['dteday'])

# Mapping season untuk visualisasi yang lebih jelas
season_mapping = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
df_day['season_label'] = df_day['season'].map(season_mapping)

# Sidebar
st.sidebar.title("Bike Sharing Dashboard")
st.sidebar.subheader("Filter Data")

# Fitur interaktif: Filter berdasarkan Rentang Tanggal
start_date = st.sidebar.date_input("Pilih Tanggal Awal", df_day['dteday'].min())
end_date = st.sidebar.date_input("Pilih Tanggal Akhir", df_day['dteday'].max())

# Pastikan start_date selalu lebih kecil atau sama dengan end_date
if start_date > end_date:
    st.sidebar.error("Tanggal awal harus lebih kecil dari tanggal akhir.")

# Fitur interaktif: Filter berdasarkan musim (season)
selected_season = st.sidebar.multiselect(
    "Pilih Musim",
    df_day['season_label'].unique(),
    default=df_day['season_label'].unique()
)

# Filter Data Berdasarkan Pilihan Pengguna
df_filtered = df_day[
    (df_day['dteday'] >= pd.to_datetime(start_date)) &
    (df_day['dteday'] <= pd.to_datetime(end_date)) &
    (df_day['season_label'].isin(selected_season))
]

# Judul Dashboard
st.title("📊 Bike Sharing Analysis")

# **Visualisasi 1: Tren Peminjaman Sepeda dari Waktu ke Waktu**
st.subheader("🔹 Tren Peminjaman Sepeda")

fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(x='dteday', y='cnt', data=df_filtered, color='blue', ax=ax)
ax.set_xlabel("Tanggal")
ax.set_ylabel("Jumlah Peminjaman Sepeda")
ax.set_title("Tren Peminjaman Sepeda dari Waktu ke Waktu")
st.pyplot(fig)

# **Visualisasi 2: Pengaruh Hari Kerja vs Hari Libur terhadap Peminjaman Sepeda**
st.subheader("🔹 Perbandingan Peminjaman Sepeda pada Hari Kerja dan Hari Libur")

fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x='workingday', y='cnt', data=df_filtered, palette=['red', 'green'], ax=ax)
ax.set_xlabel("Hari Kerja (0 = Libur, 1 = Hari Kerja)")
ax.set_ylabel("Jumlah Peminjaman Sepeda")
ax.set_title("Distribusi Peminjaman Sepeda Berdasarkan Hari Kerja")
st.pyplot(fig)

# **Visualisasi 3: Rata-rata Peminjaman Sepeda Berdasarkan Musim**
st.subheader("🔹 Rata-rata Peminjaman Sepeda Berdasarkan Musim")

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x='season_label', y='cnt', data=df_filtered, palette='coolwarm', ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Rata-rata Peminjaman Sepeda")
ax.set_title("Jumlah Peminjaman Sepeda Berdasarkan Musim")
st.pyplot(fig)

# **Visualisasi 4: Korelasi Faktor terhadap Jumlah Peminjaman Sepeda**
st.subheader("🔹 Korelasi Faktor dengan Peminjaman Sepeda")

# Pilih kolom numerik untuk korelasi
df_corr = df_filtered.select_dtypes(include=[np.number])

fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(df_corr.corr(), annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
ax.set_title("Matriks Korelasi Antar Variabel")
st.pyplot(fig)

# Menampilkan Data yang Sudah Difilter
st.subheader("📌 Data yang Ditampilkan Berdasarkan Filter")
st.dataframe(df_filtered[['dteday', 'season_label', 'cnt', 'workingday']].head(10))

