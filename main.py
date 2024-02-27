# llama = LlamaAPI("LL-D0am6EV0l1IeshE15ysSrlPMpqr5Z6rxxaBVgo2bcTvahIR2NZBWhrzkZpPbzoOP")
# model = ChatLlamaAPI(client=llama)
# from llamaapi import LlamaAPI
# from langchain_experimental.llms import ChatLlamaAPI

import streamlit as st

st.title("Sweet style")

st.set_page_config(page_title="AI-assistant", page_icon="📊")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
  with st.chat_message("user"):
        st.markdown(prompt)
  st.session_state.messages.append({"role": "user", "content": prompt})

response = "Ha"
with st.chat_message("assistant"):
    st.markdown(response)
st.session_state.messages.append({"role": "assistant", "content": response})



    

