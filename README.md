# Gemini Powered AI Streamlit App
A simple Streamlit web application that integrates with Google’s Gemini Generative AI models to generate text responses based on user prompts.

📌 Features
• 	Interactive UI built with Streamlit.
• 	Secure API key management using dotenv.
• 	Integration with Google Generative AI ().
• 	Supports current Gemini models (e.g., , , ).
• 	Error handling for invalid prompts or API issues.

## Tech

- python

# Libs

- google.generativeai
- streammil

# How to Run

## Create Virtual Environment
### Creating a virtual environment 
- Navigate to your project folder
- Create the virtual environment:
- python -m venv venv
### Activate virtual Environment
- venv\Scripts\activate
### Execute App
- python -m streamlit run ai-app.py  to start the app

### Install Dependencies
- pip install -r requirements.txt

# To check all avilable models to Use
- python supported_models.py run this

# Deactive Env when done
- deactivate
