from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    response= model.generate_content(question)
    return response.text

st.set_page_config(page_title="Q&A Demo")

st.header("Gokul's ChatBot LLM Powered by XYZ")

input = st.text_input("Input: ",key="input")
name = st.text_input("Enter Your name ")

submit = st.button("Ask the question")

if submit:
        st.write(f'Hello {name}\n This is your output')
        # st.write(f'Since it is for {reason} purpose we are allowing your request')
        response=get_gemini_response(input)
        st.subheader("The response is")
        st.write(response)