import streamlit as st
from llamaapi import LlamaAPI
from langchain_experimental.llms import ChatLlamaAPI

llama = LlamaAPI("LL-D0am6EV0l1IeshE15ysSrlPMpqr5Z6rxxaBVgo2bcTvahIR2NZBWhrzkZpPbzoOP")
model = ChatLlamaAPI(client=llama)

st.title("Sweet style")

option = st.selectbox("What would you like to generate?",
                     ['Text', 'Image'])

if option == "Text":
  prompt = st.text_input("Enter your text prompt here", "")
  if st.button('Submit') and not prompt:
    st.warning("Please write a prompt", icon="⚠️")
  else:
    pass
      
elif option == "Image":
  prompt = st.text_input("Enter your image prompt here", "")
  if st.button('Submit') and not prompt:
    st.warning("Please write a prompt", icon="⚠️")
  else:
    pass
