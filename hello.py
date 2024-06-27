from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
from langchain import PromptTemplate

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

job_template = PromptTemplate(
    input_variables=["details"],
    template="""
    You need to provide comprehensive and detailedjob description(JD) for candidates interested in  a given job whose rough details are
    {details}
    Given below are the points you need to mention in the job description. If any of them is provided in input, use it, else generate it yourself
    - Job Title 
    - Years of Experience required
    - Salary Offered
    - A brief overview of the role
    - Detailed Roles and Responsibilities(if provided, else think it yourself about this role and generate)
    - Required Skills and Qualifications(if provided, else think it yourself about this role and generate)
    - Benefits and Perks(if provided)
    - Location (if provided, else write 'Location details will be shared with selected candidates')
    Don't mention any other irrelevant points. Be concise and follow the given format
    
    Ensure the job description is attractive to potential candidates and SEO-friendly. Include relevant SEO keywords at the end.
    """
)

def get_gemini_response(question, model_name):
    model = genai.GenerativeModel(model_name)
    response = model.generate_content(question)
    return response.text

available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods and 'vision' not in m.name]
st.set_page_config(page_title="Gemini Response")
st.header("Gemini LLM Application")
selected_model = st.selectbox("Select Gemini Model", available_models)
input_details = st.text_area("Input: ", key="input")
submit = st.button("Generate Job Description")

if submit:
    response = get_gemini_response(input_details, selected_model)
    st.write(response)
