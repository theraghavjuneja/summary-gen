import pandas as pd
import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def load_csv_data(file_path):
    df = pd.read_csv(file_path)
    return df

prompt_template = """
Here is the information about the students and their projects:

{csv_data}

Now, I have a question:
{question}
"""

def format_prompt(csv_data, question):
    return prompt_template.format(csv_data=csv_data, question=question)

def df_to_string(df):
    return df.to_string(index=False)

def get_gemini_response(question, csv_data, model_name):
    prompt = format_prompt(csv_data, question)
    model = genai.GenerativeModel(model_name)
    response = model.generate_content(prompt)
    return response.text

csv_file_path = 'data_updated.csv'  # Replace with the actual path to your CSV file
data = load_csv_data(csv_file_path)
csv_string = df_to_string(data)

# Example question
question = "I want to know about those students which have worked on AI or Artificial Intelligence related projects."


response = get_gemini_response(question, csv_string, 'gemini-1.5-flash-latest')  # Replace 'gemini-model-name' with the actual model name
print(response)
