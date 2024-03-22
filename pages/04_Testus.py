import streamlit as st
from langchain.chat_models import GigaChat
from langchain.schema import ChatMessage

CREDENTIALS = st.secrets["CREDENTIALS"]
chat = GigaChat(credentials=CREDENTIALS, verify_ssl_certs=False)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        ChatMessage(
            role="system",
            content="Ты - умный ИИ ассистент, который специализируется на экономических, технических вопросах развития шоколадного бизнеса.",
        ),
        ChatMessage(role="assistant", content="Как я могу помочь вам?"),
    ]

for message in st.session_state.messages:
    with st.chat_message(message.role):
        st.markdown(message.content)

if prompt := st.chat_input():
    message = ChatMessage(role="user", content=prompt)
    st.session_state.messages.append(message)

    with st.chat_message(message.role):
        st.markdown(message.content)

    message = ChatMessage(role="assistant", content="")
    st.session_state.messages.append(message)

    with st.chat_message(message.role):
        message_placeholder = st.empty()
        for chunk in chat.stream(st.session_state.messages):
            message.content += chunk.content
            message_placeholder.markdown(message.content + "▌")
        message_placeholder.markdown(message.content)
