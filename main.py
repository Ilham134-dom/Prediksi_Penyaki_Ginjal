# Import library yang dibutuhkan
import streamlit as st
from web_function import load_data
from Tabs import home, predict, visualise  # Pastikan modul Tabs memiliki file home.py, predict.py, dan visualise.py

# Dictionary untuk mapping tabs
Tabs = {
    "Home": home,
    "Prediction": predict,
    "Visualisation": visualise
}

# Membuat sidebar navigasi
st.sidebar.title("Navigasi")

# Membuat radio option untuk navigasi halaman
page = st.sidebar.radio("Pilih Halaman", list(Tabs.keys()))

# Load dataset menggunakan fungsi load_data
try:
    df, x, y = load_data()
except Exception as e:
    st.error(f"Gagal memuat data: {e}")
    st.stop()

# Kondisi untuk memanggil fungsi app dari masing-masing halaman
if page in ["Prediction", "Visualisation"]:
    try:
        Tabs[page].app(df, x, y)  # Pastikan setiap modul memiliki fungsi app(df, x, y)
    except Exception as e:
        st.error(f"Terjadi error pada halaman {page}: {e}")
else:
    try:
        Tabs[page].app()  # Pastikan modul home hanya memerlukan fungsi app() tanpa parameter
    except Exception as e:
        st.error(f"Terjadi error pada halaman {page}: {e}")
