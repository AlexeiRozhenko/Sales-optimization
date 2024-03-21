import streamlit as st
from langchain.chat_models import GigaChat
from langchain.schema import ChatMessage

CREDENTIALS = st.secrets["CREDENTIALS"]
chat = GigaChat(credentials=CREDENTIALS, verify_ssl_certs=False)

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hello! How can I help you?"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Enter your prompt here"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chat(st.session_state["messages"])
            # response = chat.generate([ChatMessage(content=prompt)])
            st.markdown(response.content)
        message = {"role": "assistant", "content": response.content}
    st.session_state.messages.append(message)




  
