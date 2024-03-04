import streamlit as st
def kalkulatorsegitiga():
    st.title('Hitung Luas segitiga')
    panjang = st.number_input("Masukkan Nilai Panjang", 0)
    tinggi = st.number_input("Masukkan Nilai tinggi", 0)
    hitung = st.button("Hitung Luas")
    
    if hitung:
        luas = panjang * tinggi /2
        st.success(f"Luas Segitiga adalah={luas}")