import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

for m in genai.list_models():
    print(m.name, "supports:", m.supported_generation_methods)