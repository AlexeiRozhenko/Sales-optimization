import streamlit as st
import requests
import io
from PIL import Image
# with st.sidebar:
#     option = st.selectbox(
#         'Which model would you like to use?',
#         ('GigaChat', 'Another one (no Russian)'))
# if option == "GigaChat":
API_TOKEN = st.secrets["TOKEN"]
API_URL = "https://api-inference.huggingface.co/models/digiplay/AbsoluteReality_v1.8.1"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
	
prompt = st.text_input('What would you like to draw?', 'Chocolate bar design, cinematic')
if st.button("Generate image"):
  image_bytes = query({
	"inputs": f"{prompt}",})
  image = Image.open(io.BytesIO(image_bytes))
  st.image(image, caption='Prompt result', width=400)
  

