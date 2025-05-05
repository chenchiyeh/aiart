import os
import requests
from dotenv import load_dotenv

# Load Hugging Face token from .env file
load_dotenv()
HF_TOKEN = os.getenv("HUGGINGFACE_API_KEY")

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
    style = ["formal", "casual", "sporty", "vintage", "modern"]
    print("Pick a style genre for your clothing image:")
    for idx, genre in enumerate(style, 1):
        print(f"{idx}. {genre.capitalize()}")

    while True:
        try:
            choice = int(input("Enter the number of your chosen genre: "))
            if 1 <= choice <= len(style):
                selected_genre = style[choice - 1]
                break
            else:
                print("⚠️ Please choose a valid number.")
        except ValueError:
            print("⚠️ Please enter a number.")

    preset = (
        f"Create a clear, high-resolution image of a single {selected_genre} clothing item.\n"
        "The clothing is displayed on a standard hanger, centered in the frame.\n"
        "It is hanging against a smooth white studio background with even lighting.\n"
        "No other objects or clothing are present in the image.\n"
        "The entire clothing item should be fully visible, cleanly framed, and easy to identify.\n"
        "No people, mannequins, shadows, or decorative elements.\n"
        "The clothing item is: "
    )



    user_input = input("🧥 Describe your clothing piece: ")
    prompt = preset + user_input

    print(f"📸 Generating a {selected_genre} clothing image...")
    generate_image(prompt)