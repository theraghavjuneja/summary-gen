import pandas as pd
import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

csv_file_path = 'csvforgemini.csv'
df = pd.read_csv(csv_file_path)

data_dict = df.to_dict(orient='records')

def create_prompt(query):
    prompt_template = """
    You are given a dataset of problem statements with the following columns: S.NO., PS CATEGORY, problem statement title, Domain Bucket.
    Based on the query below, extract the relevant information from the dataset.
    Yoir only aim is to return the S.No. of matching projects from the query, If no project match simply say "Sorry, no resuls found"
    Also look for matching synonyms of the query in the problem statements. 
    For example: If the user is asking about Artificial Intelligence based problem statements, you can look for AI,ML,Artificial Intelligence,DL,Deep Learning . Also try to interpret the problem statement
    to determine whether it uses AI or not
    Query: {query}

    Dataset:
    {data}

    Provide the answer in a clear and concise format.
    """
    data_str = "\n".join([f"{row['S.NO.']}, {row['PS CATEGORY']}, {row['problem statement title']}, {row['Domain Bucket']}" for row in data_dict])
    return prompt_template.format(query=query, data=data_str)

def get_gemini_response(question, model_name):
    model = genai.GenerativeModel(model_name)
    response = model.generate_content(question)
    return response.text

def process_query(query, model_name="gemini-1.5-flash-latest"):
    prompt = create_prompt(query)
    response_text = get_gemini_response(prompt, model_name)
    return response_text

# Example usage
query = "Artifical Intelligence based problem statements"
response = process_query(query)
print(response)
numbers = list(map(int, response.split(', ')))
