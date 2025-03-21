Deskripsi Proyek
Proyek ini adalah dashboard interaktif yang dikembangkan menggunakan Streamlit 
untuk menganalisis dataset Bike Sharing. Dashboard ini memungkinkan pengguna untuk 
mengeksplorasi berbagai aspek dari data peminjaman sepeda, termasuk overview data, 
analisis distribusi, faktor yang mempengaruhi, clustering, dan analisis time series.

Persyaratan
Sebelum menjalankan proyek ini, pastikan Anda memiliki:
- Python 3.x terinstal
- Paket Python berikut:
  - streamlit
  - pandas
  - numpy
  - matplotlib
  - seaborn

Jika belum terinstal, Anda dapat menginstalnya dengan perintah berikut:
pip install streamlit pandas numpy matplotlib seaborn

Cara Menjalankan Dashboard
1. Kloning atau Unduh Repositori
   git clone (https://github.com/BondanTriWibowo06/analisisdata/edit/main/)
   cd repo-name
2. Jalankan Dashboard
   streamlit run main.py
3. Unggah Dataset
   - Setelah dashboard terbuka di browser, unggah file day.csv dan hour.csv pada sidebar.
   - Setelah file diunggah, Anda bisa mulai melakukan eksplorasi data melalui navigasi sidebar.

Struktur Menu Dashboard
- Overview Data: Menampilkan ringkasan dataset.
- Analisis Peminjaman Sepeda: Visualisasi distribusi jumlah peminjaman sepeda.
- Faktor yang Mempengaruhi: Analisis korelasi antara variabel.
- Clustering Binning: Pengelompokan peminjaman sepeda berdasarkan kategori tertentu.
- Time Series Analysis: Analisis tren peminjaman sepeda dari waktu ke waktu.

Deployment ke Streamlit Cloud
Untuk melakukan deploy ke Streamlit Cloud, ikuti langkah berikut:
1. Upload kode ke GitHub
2. Buka Streamlit Cloud dan login.
3. Buat aplikasi baru:
   - Hubungkan ke repository GitHub.
   - Pilih branch yang berisi kode.
   - Atur path ke Bike_Sharing_Analysis.py.
   - Klik "Deploy" dan tunggu hingga proses selesai.

4. Gunakan Dashboard
   - Akses aplikasi melalui URL yang diberikan oleh Streamlit Cloud.
   - Unggah dataset dan eksplorasi data seperti pada langkah lokal.
