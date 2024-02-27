import streamlit as st

st.title("Sweet style")

model = st.selectbox("What would you like to generate?",
                     ['Text', 'Image'])

if model == "Text":
  prompt = st.text_input("Enter your prompt here", "")
  if st.button('Submit') and not prompt:
    st.warning("Please enter a prompt", icon="⚠️")
  else:
    pass
      
elif model == "Image":
  prompt = st.text_input("Enter your prompt here", "")
  if st.button('Submit') and not prompt:
    st.warning("Please enter a prompt", icon="⚠️")
  if st.button('Submit'):
      pass
