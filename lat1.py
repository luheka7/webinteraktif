import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt
st.write("Nilai Ujian 2024")
df = pd.DataFrame({
    'No': [1,2,3,4],
    'Nama':['zea','feli','natax','tiel'],
    'nilai':[88,80,84,76]
})

df