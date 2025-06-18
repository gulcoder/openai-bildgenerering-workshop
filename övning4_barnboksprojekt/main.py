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

base_prompt = "A small curious elephant exploring a jungle, children book illustration style"
variations = [
    base_prompt + ", elephant looking at butterfiles",
    base_prompt + ", elephant crossing a small river",
    base_prompt + ", elephant meeting jungle friends",
    base_prompt + ", elephant under a big tree",
    base_prompt + ", elephant plaing with colorful birds"
    ]

print("Genererar barnbok-bilder...")
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
    