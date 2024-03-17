import streamlit as st
import requests
import io
from PIL import Image
# with st.sidebar:
#     option = st.selectbox(
#         'Which model would you like to use?',
#         ('GigaChat', 'Another one (no Russian)'))
# if option == "GigaChat":

prompt = st.text_input('What would you like to draw?', 'Chocolate bar design, cinematic')

API_URL = "https://api-inference.huggingface.co/models/digiplay/AbsoluteReality_v1.8.1"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
image_bytes = query({
	"inputs": f"{prompt}",
})
# You can access the image with PIL.Image for example
image = Image.open(io.BytesIO(image_bytes))

st.image(image, caption='Prompt result')
  

