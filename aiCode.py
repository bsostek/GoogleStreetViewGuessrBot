import google.generativeai as genai
from constants import GEMINI_API_KEY,PROMPT

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain how AI works")

def getLocation(image):
    response = model.generate_content([PROMPT,image])
    return response.text

