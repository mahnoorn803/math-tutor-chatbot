
import openai
import streamlit as st
from googletrans import Translator

# OpenAI API Key (replace with your own)
openai.api_key = "your-api-key-here"

st.title("🌍 AI Math Tutor Chatbot")
st.write("Ask me a math question! I'll explain it step by step.")

# Select a language
languages = {"English": "en", "Spanish": "es", "French": "fr", "German": "de", "Chinese": "zh-cn"}
selected_language = st.selectbox("Choose your language:", list(languages.keys()))

# Get user input
user_input = st.text_input("Type your math question:")

def get_math_explanation(question):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a friendly math tutor who explains concepts step by step."},
            {"role": "user", "content": question}
        ]
    )
    return response["choices"][0]["message"]["content"]

def translate_text(text, target_language):
    translator = Translator()
    return translator.translate(text, dest=target_language).text

if user_input:
    explanation = get_math_explanation(user_input)
    translated_explanation = translate_text(explanation, languages[selected_language])
    st.write(translated_explanation)
