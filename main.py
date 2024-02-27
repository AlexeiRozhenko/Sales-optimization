import streamlit as st

st.title("Sweet style")

model = st.selectbox("What would you like to generate?",
                     ['Text', 'Image'])
with model:
    if model == "Text":
        prompt = st.text_input("Enter your prompt here", "")
        if st.button('Submit'):
            pass
          
    if model == "Image":
        prompt = st.text_input("Enter your prompt here", "")
        if st.button('Submit'):
            pass
