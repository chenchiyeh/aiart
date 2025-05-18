import os
import requests
import base64
import replicate
from dotenv import load_dotenv

# Load API token from .env
load_dotenv()
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

# Authenticate
client = replicate.Client(api_token=REPLICATE_API_TOKEN)



if __name__ == "__main__":
    
    file_input = open("./clothing.png", "rb")

    user_prompt = input("🧥 Describe your edit: ")
    user_prompt = "Make this clothing piece cartoon style"
    input = {
        "image": file_input,
        "prompt": user_prompt
    }

    output = replicate.run(
        "zsxkib/step1x-edit:12b5a5a61e3419f792eb56cfc16eed046252740ebf5d470228f9b4cf2c861610",
        input=input
    )
    with open("output.webp", "wb") as file:
        file.write(output.read())
