import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Use the active gemini-3.8-flash endpoint
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Say hello"
)

print("SUCCESS!")
print(response.text)