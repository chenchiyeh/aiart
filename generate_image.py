import os
import requests
from dotenv import load_dotenv

# Load Hugging Face token from .env file
load_dotenv()
HF_TOKEN = os.getenv("HUGGINGFACE_API_KEY")

# API URL for stable-diffusion-v1-5 model
API_URL = "https://api-inference.huggingface.co/models/stable-diffusion-v1-5/stable-diffusion-v1-5"
HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"}

def generate_image(prompt):
    response = requests.post(API_URL, headers=HEADERS, json={"inputs": prompt})
    if response.status_code == 200:
        with open("generated_image.png", "wb") as f:
            f.write(response.content)
        print("Image saved as 'generated_image.png'")
    else:
        print("Error:", response.status_code, response.text)

if __name__ == "__main__":
    prompt = "A futuristic city skyline at sunset"
    generate_image(prompt)
