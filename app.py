from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
from langchain import PromptTemplate

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

# Define a LangChain prompt template for a hackathon description
hackathon_template = PromptTemplate(
    input_variables=["description"],
    template="""You are organizing a hackathon. Provide a rough description based on the following details:
    {description}
    """
)

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Set up Streamlit app
st.set_page_config(page_title="Gemini Response")
st.header("Gemini LLM Application")

input_description = st.text_input("Input: ", key="input")
submit = st.button("Provide the rough description")

if submit:
    # Format the input with the LangChain prompt template
    formatted_prompt = hackathon_template.format(description=input_description)
    response = get_gemini_response(formatted_prompt)
    st.subheader("The response is")
    st.write(response)
