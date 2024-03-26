import streamlit as st
import requests
import json
import time
import io
from PIL import Image
import base64

KANDINSKY_API = st.secrets["KANDINSKY_API"]
KANDINSKY_SECRET = st.secrets["KANDINSKY_SECRET"]

class Text2ImageAPI:

    def __init__(self, url, api_key, secret_key):
        self.URL = url
        self.AUTH_HEADERS = {
            'X-Key': f'Key {api_key}',
            'X-Secret': f'Secret {secret_key}',
        }

    def get_model(self):
        response = requests.get(self.URL + 'key/api/v1/models', headers=self.AUTH_HEADERS)
        data = response.json()
        return data[0]['id']

    def generate(self, prompt, model, images=1, width=1024, height=1024):
        params = {
            "type": "GENERATE",
            "numImages": images,
            "width": width,
            "height": height,
            "generateParams": {
                "query": f"{prompt}"
            }
        }

        data = {
            'model_id': (None, model),
            'params': (None, json.dumps(params), 'application/json')
        }
        response = requests.post(self.URL + 'key/api/v1/text2image/run', headers=self.AUTH_HEADERS, files=data)
        data = response.json()
        return data['uuid']

    def check_generation(self, request_id, attempts=10, delay=10):
        while attempts > 0:
            response = requests.get(self.URL + 'key/api/v1/text2image/status/' + request_id, headers=self.AUTH_HEADERS)
            data = response.json()
            if data['status'] == 'DONE':
                return data['images']
            attempts -= 1
            time.sleep(delay)
    
    def image_generation(image):
        image_base64 = image[0]
        image_data = base64.b64decode(image_base64)
        with open("prompt_result.jpg", "wb") as file:
            file.write(image_data)
            return file

if __name__ == '__main__':
	prompt = st.text_input('What would you like to draw?', 'Chocolate bar design, cinematic')
	if prompt and st.button("Generate image"):
        api = Text2ImageAPI('https://api-key.fusionbrain.ai/', KANDINSKY_API, KANDINSKY_SECRET)
		model_id = api.get_model()
		uuid = api.generate(f"{prompt}", model_id)
		image = api.check_generation(uuid)
		file = api.image_generation(image)
		st.image(file, caption='Prompt result')
	
