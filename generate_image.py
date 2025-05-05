import os
import requests
from dotenv import load_dotenv

# Load Hugging Face token from .env file
load_dotenv()
HF_TOKEN = os.getenv("HUGGINGFACE_API_KEY")


#preset
preset = (
    "A clear and well-lit image of a single clothing item hanging in a white, empty room. "
    "The clothing is displayed on a hanger, with no people or distractions in the background. "
    "No logos or text. Only one item of clothing is shown. "
    "The clothing is: "
)


# API URL for stable-diffusion-v1-5 model
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
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
    
    user_input = input(" Describe your clothing piece: ")
    prompt = preset + user_input

    generate_image(prompt)