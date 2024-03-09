import streamlit as st
from page1 import page_1
from page2 import page_2
from page3 import page_3
from image1 import main
from kalkulatorluas import kalkulatorsegitiga
# import pandas as pd
# # import matplotlib.pyplot as plt
# st.write("Nilai Ujian 2024")
# df = pd.DataFrame({
#     'No': [1,2,3,4],
#     'Nama':['zea','feli','natax','tiel'],
#     'nilai':[88,80,84,76]
# })

# df
    
PAGES = {
    "Home" : page_1,
    "Page 2" : page_2,
    "Page 3" : page_3,
    "Kalkulator luas" : kalkulatorsegitiga,
    "Konversi foto" : main
    }

st.sidebar.image("foto.png", width=150)
page = st.sidebar.radio("Halaman", list(PAGES.keys()))
PAGES[page]()

st.markdown(
    """
            <style>
            [data-testid="stActionButtonIcon"]{
                display : none;
            }
            [data-testid="baseButton-header"]{
                display : none;
            }
            
            </style>
            """,
    unsafe_allow_html=True,
)
    