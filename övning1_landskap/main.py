import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("OPENAI_API_KEY")

if not api_key:
    print("Lägg till din OPENAI_API_KEY i .env-filen.")
    exit(1)

client = OpenAI(api_key=api_key)

prompt ="A serene mountain landscape with a clear lake and dense pine forest, realistic style"

response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    n=1,
    size="1024x1024"
)

image_url = response.data[0].url
print(f"\n Bilden är genererad!\nURL: {image_url}")
