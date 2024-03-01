# llama = LlamaAPI("LL-D0am6EV0l1IeshE15ysSrlPMpqr5Z6rxxaBVgo2bcTvahIR2NZBWhrzkZpPbzoOP")
# model = ChatLlamaAPI(client=llama)
# from llamaapi import LlamaAPI
# from langchain_experimental.llms import ChatLlamaAPI

import streamlit as st
import openai
from openai import OpenAI

st.header("Sweet style")

# st.set_page_config(page_title="AI-assistant", page_icon="📊")

if messages not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hello! How can I help you?"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Enter your prompt here"):
  with st.chat_message("user"):
        st.markdown(prompt)
  st.session_state.messages.append({"role": "user", "content": prompt})

openai.api_key = "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"
response = openai.ChatCompletion.create(model = 'gpt-3.5-turbo', temperature = 1, 
                                        messages = [f"{{'role': 'user', 'content': '{message}'}}"])
msg = response.choices[0]["message"]["content"]

with st.chat_message("assistant"):
    st.markdown(msg)
st.session_state.messages.append({"role": "assistant", "content": response})



    

