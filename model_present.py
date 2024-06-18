from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
from langchain import PromptTemplate
os.getenv("GOOGLE_API_KEY")
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)