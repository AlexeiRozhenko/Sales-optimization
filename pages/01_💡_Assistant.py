import streamlit as st
import hugchat
from hugchat.login import Login

hf_email = st.secrets['EMAIL']
hf_pass = st.secrets['PASS']

def generate_response(prompt, email, passwd):
    # Hugging Face Login
    sign = Login(email, passwd)
    cookies = sign.login()
    # Create ChatBot                        
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    return chatbot.chat(prompt)

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hello! How can I help you?"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Enter your prompt here"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

with st.chat_message("assistant"):
    with st.spinner("Thinking..."):
        response = generate_response(prompt, hf_email, hf_pass) 
        st.write(response)
    message = {"role": "assistant", "content": response}
st.session_state.messages.append({"role": "assistant", "content": response})




    
