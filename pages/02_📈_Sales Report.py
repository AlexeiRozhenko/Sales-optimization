import streamlit as st 
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Sales report", page_icon="📈")

with open(os.path.join('pages','sample_file.xlsx'),'r') as file:
  st.download_button(label= 'Download Sample File',
                    file_name='sample_file.xlsx',
                    data=file,
                    use_container_width=True)

uploaded_file = st.file_uploader("Choose an XLSX file", accept_multiple_files=False)
if uploaded_file is not None:
  df = pd.read_excel(uploaded_file)
