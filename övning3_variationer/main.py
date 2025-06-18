import os
from openai import OpenAI
from dotenv import load_dotenv

# Ladda miljövariabler
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("❗ Du måste ange din OPENAI_API_KEY i .env-filen.")
    exit(1)

# Skapa klient
client = OpenAI(api_key=api_key)

base_prompt = "A futuristic electric car design, 3D render"
variations = [
    base_prompt + ", red color",
    base_prompt + ", blue color",
    base_prompt + ", nighttime city background",
    base_prompt + ", bird's eye view",
    base_prompt + ", sleek and aerodynamic style"
    ]

print("Genererar bilder...")
for i, prompt in enumerate(variations, start=1):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response.data[0].url 
    print(f"Bild {i} ({prompt}): {image_url}")

if __name__ == "__main__":
    import os
    

