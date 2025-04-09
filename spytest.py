import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('data-perceraian.csv', sep=';')
if data.isnull().values.any():
    st.warning('Data mengandung nilai kosong. Harap periksa kembali dataset Anda.')


# Judul Dashboard
st.title('Dashboard Data Perceraian di Indonesia')

# Tampilkan 5 data pertama
st.subheader('Data Awal')
st.dataframe(data.head())

# Statistik Deskriptif
st.subheader('Statistik Deskriptif')
st.write(data.describe())

# Pilih Provinsi
provinsi = st.selectbox('Pilih Provinsi:', data['nama_provinsi'].unique())
data_filtered = data[data['nama_provinsi'] == provinsi]
if data_filtered.empty:
    st.warning(f'Tidak ada data untuk provinsi {provinsi}.')
else:
    # Lanjutkan dengan visualisasi


# Visualisasi jumlah perceraian per tahun
 st.subheader(f'Jumlah Perceraian di {provinsi} per Tahun')
 fig, ax = plt.subplots()
 data_filtered.groupby('tahun')['jumlah_perceraian'].sum().plot(kind='bar', ax=ax)
 plt.ylabel('Jumlah Perceraian')
 plt.xlabel('Tahun')
 st.pyplot(fig)

# Visualisasi penyebab perceraian
 st.subheader(f'Penyebab Perceraian di {provinsi}')
 fig2, ax2 = plt.subplots()
 data_filtered['faktor_penyebab'].value_counts().plot(kind='barh', ax=ax2)
 plt.xlabel('Jumlah Kasus')
 st.pyplot(fig2)
