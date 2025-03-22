import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Dataset default
default_day_data = {
    'dteday': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05'],
    'cnt': [120, 150, 180, 200, 220]
}

default_hour_data = {
    'dteday': ['2021-01-01 00:00', '2021-01-01 01:00', '2021-01-01 02:00', '2021-01-01 03:00', '2021-01-01 04:00'],
    'cnt': [5, 10, 15, 20, 25]
}

df_day = pd.DataFrame(default_day_data)
df_hour = pd.DataFrame(default_hour_data)

def main():
    st.title("Bike Sharing Dashboard")
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

if __name__ == "__main__":
    main()
