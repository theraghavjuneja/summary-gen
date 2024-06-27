import pandas as pd
df=pd.read_csv('csvforgemini.csv')
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    words = word_tokenize(text)
    words = [word for word in words if word not in stopwords.words('english')]
    return ' '.join(words)
df['Processed Statement'] = df['problem statement title'].apply(preprocess_text)
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

df['Embedding'] = df['Processed Statement'].apply(lambda x: model.encode(x, convert_to_tensor=True))

def rank_problem_statements(query):
    query_processed = preprocess_text(query)
    query_embedding = model.encode(query_processed, convert_to_tensor=True)
    similarities = df['Embedding'].apply(lambda x: util.pytorch_cos_sim(query_embedding, x).item())
    ranked_indices = similarities.argsort()[::-1]
    return df.iloc[ranked_indices]['S.NO.'].tolist()


query = "I need someone who has worked on AI related chatbot in healthcare"
ranked_serial_numbers = rank_problem_statements(query)
print(ranked_serial_numbers)
