import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API client
genai.configure(api_key=API_KEY)

# Use a current, stable model
model = genai.GenerativeModel("models/gemini-2.5-flash")

# Streamlit App
st.set_page_config(page_title="Gemini Powered", layout="centered")
st.title("How Can I Help You Today ?")

st.subheader("Enter a prompt")

prompt = st.text_area(
    "Prompt",
    height=150,
    placeholder="Example: Write a short story about time travel"
)

if st.button("Generate Response"):
    if not prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Generating response…"):
            try:
                response = model.generate_content(prompt)
                st.subheader("Generated Response")
                st.write(response.text)
            except Exception as error:
                st.error(f"An error occurred: {error}")
