from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
from langchain import PromptTemplate


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# model = genai.GenerativeModel("gemini-pro")

detailed_template = PromptTemplate(
    input_variables=["description"],
    template="""
    You are organizing a hackathon. Based on the following details:
    {description}

    Please provide a comprehensive and detailed description of the hackathon including:
    - Hackathon name
    - Tagline (if provided, else generate one)
    - A brief overview
    - Objectives (if provided, else create them)
    - Eligibility criteria (if provided, else create them)
    - Prizes (if provided, else write 'Prizes are ...')
    - Phases and Timeline (if provided)
    - Who should participate(For example, if it is a blockchain based hackathon, You can write Participation is open to all, But those who are interested in blockchain based hackathon and know blockchain must participate)
    Also, make sure that provided response is attractive to the hackathon participants
    You can make more subheaders if necessary 
    Additionally, ensure the content is SEO-friendly and include relevant SEO keywords at the end.
    """
)

summary_template = PromptTemplate(
    input_variables=["description"],
    template="""
    You are organizing a hackathon. Based on the following details:
    {description}

    If you input provided is quite comprehensive. Please provide a very detailed summary including:
    - Hackathon name
    - Tagline (if provided, else generate one)
    - A brief overview
    - Objectives (if provided, else create them)
    - Eligibility criteria (if provided, else create them)
    - Prizes (if provided, else write 'Prizes are ...')
    - Phases and Timeline (if provided)
    - Who should participate(For example, if it is a blockchain based hackathon, You can write Participation is open to all, But those who are interested in blockchain based hackathon and know blockchain must participate)
    Also, make sure that provided response is attractive to the hackathon participants
    
    You can make more subheaders according to the provided input , if necessary
    
    Additionally, ensure the content is SEO-friendly and include relevant SEO keywords at the end.
    """
)

def get_gemini_response(question,model_name):
    model=genai.GenerativeModel(model_name)
    response = model.generate_content(question)
    return response.text

def determine_template(description):
    if len(description.split()) > 50:  # Threshold for determining if input is long or short
        return summary_template
    else:
        return detailed_template

available_models=[m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods and 'vision' not in m.name ]
st.set_page_config(page_title="Gemini Response")
st.header("Gemini LLM Application")
selected_model = st.selectbox("Select Gemini Model", available_models)
input_description = st.text_area("Input: ", key="input")
submit = st.button("Generate Hackathon Description")

if submit:
    selected_template = determine_template(input_description)
    formatted_prompt = selected_template.format(description=input_description)
    response = get_gemini_response(formatted_prompt,selected_model)
    st.subheader("The response is")
    st.write(response)


import matplotlib.pyplot as plt

models = ["Gemma 7B", "Gemma 2B", "Mistral 7B", "LLama 2 13B", "Llama 2 7B"]
scores = [64.3, 42.3, 62.5, 54.8, 45.3]

# Create the bar chart
plt.figure(figsize=(10, 6))
plt.bar(models, scores, color='skyblue')
plt.xlabel('Models')
plt.ylabel('MMLU Scores')
plt.title('MMLU Scores of Different Models')
plt.ylim(0, 70)

st.pyplot(plt)
