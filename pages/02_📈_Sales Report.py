import streamlit as st 
import plotly.express as px

st.set_page_config(page_title="Sales report", page_icon="📈")

uploaded_file = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
if uploaded_file is not None:
  dataframe = pd.read_csv(uploaded_file)
