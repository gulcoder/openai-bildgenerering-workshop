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

# Prompt för fantasivarelsen
prompt = "A flying lion-dragon hybrid with glowing eyes and feathered wings, fantasy art style"


# Anropa DALL·E 3
response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    n=1,
    size="1024x1024"
)

# Visa bildens URL
image_url = response.data[0].url
print(f"\n🧝‍♀️ Fantasivarelsen har skapats!\nURL: {image_url}")
