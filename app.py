from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model=genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text
st.set_page_config(page_title="Gemini Response")
st.header("Gemini LLM Application")
input=st.text_input("Input: ",key="input")
submit=st.button("Provide the rough description")
if submit:
    # when submit button is clicked
    response=get_gemini_response(input)
    st.subheader("The response is")
    st.write(response)