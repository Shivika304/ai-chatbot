# gemini_service.py

import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key from .env file
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash-lite")


# -----------------------------
# Function to Generate AI Reply
# -----------------------------
def generate_response(user_message):

    # Send user message to Gemini
    response = model.generate_content(user_message)

    # Return AI text response
    return response.text