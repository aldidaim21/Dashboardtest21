import streamlit as st
from data import *


#judul dashboard
def judul():
    st.title("Dashboard Covid-19 Indonesia")
    st.write("Selamat datang di dashboard interaktif untuk menganalisis data Covid-19 di Indonesia 🔴⚪")

st.sidebar.title("Navigasi")
menu= st.sidebar.radio("Pilih Halaman",["Home","Halaman Data"])

if menu == "Home":
    #judul
    judul()
    
    df=load_data()
    #filtering
    year= select_year()
    location=select_location(df)
    df_filtered= filter_data(df, year,location)
    #kolom 1
    kolom1(df_filtered)
    pie_chart1(df_filtered)
elif menu == "Halaman Data":
    judul()
    
      
    df=load_data()
    #filtering
    year= select_year()
    location=select_location(df)
    df_filtered= filter_data(df, year,location)
    #show data
    show_data(df_filtered)
