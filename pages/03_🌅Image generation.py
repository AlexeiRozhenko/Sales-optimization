import streamlit as st

with st.sidebar:
    option = st.selectbox(
        'Which model would you like to use?',
        ('GigaChat', 'Another one (no Russian)'))

if option == "GigaChat":
  title = st.text_input('What would you like to draw?', 'Chocolate bar design, cinematic')
  

