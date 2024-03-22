import streamlit as st
from langchain.chat_models import GigaChat
from langchain.schema import ChatMessage

CREDENTIALS = st.secrets["CREDENTIALS"]
chat = GigaChat(credentials=CREDENTIALS, verify_ssl_certs=False)

# Initialize chat history
if "message" not in st.session_state:
    st.session_state.messages = [
        ChatMessage(
            role="system",
            content="Ты - умный ИИ ассистент, который специализируется на экономических, технических вопросах развития шоколадного бизнеса.",
        ),
        ChatMessage(role="assistant", content="Hello! How can I help you?"),
    ]

for message in st.session_state.messages[1::1]:
    with st.chat_message(message.role):
        st.markdown(message.content)

if prompt := st.chat_input("Enter your prompt here"):
    message = ChatMessage(role="user", content=prompt)
    with st.chat_message(message.role):
        st.markdown(message.content)
    st.session_state.messages.append(message)

    # message = ChatMessage(role="assistant", content="")
    # st.session_state.messages.append(message)

if st.session_state.messages[-1].role != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            dial = "\n".join([message.content for message in st.session_state.messages])
            response = chat(dial)
            message = ChatMessage(role="assistant", content=response.content)
            st.markdown(message.content)
    st.session_state.messages.append(message)
