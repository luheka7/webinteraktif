import streamlit as st
def page_3():
    st.title("Halaman")
    st.write("Halaman ini digunakan untuk menampilkan Halaman dari file MD(MarkDown)")
    
    with open('nama.md', 'r') as file:
        isi_teks = file.read()
    st.markdown(isi_teks)