import streamlit as st 
import plotly.express as px

st.set_page_config(page_title="Sales report", page_icon="📈")

with st.sidebar:
  uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
