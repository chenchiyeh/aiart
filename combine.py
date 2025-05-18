import os
import replicate
from dotenv import load_dotenv

# Load API token from .env
load_dotenv()
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

# Authenticate
client = replicate.Client(api_token=REPLICATE_API_TOKEN)

if __name__ == "__main__":
    print("📤 Loading avatar image...")

    file_input = open("avatar.png", "rb")

    input = {
        "image": file_input,
        "prompt": "A cartoon avatar wearing the uploaded clothing item, clean background"
    }

    print("🎨 Generating final avatar image...")

    output = client.run(
        "zsxkib/step1x-edit:12b5a5a61e3419f792eb56cfc16eed046252740ebf5d470228f9b4cf2c861610",
        input=input
    )

    # Save result
    if isinstance(output, list):
        image_url = output[0]
    else:
        image_url = output

    result = requests.get(image_url).content
    with open("final_avatar.png", "wb") as f:
        f.write(result)

    print("✅ Saved final image as final_avatar.png")
