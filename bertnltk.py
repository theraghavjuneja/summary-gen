import pandas as pd
df = pd.read_csv('csvforgemini.csv')
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from transformers import BertTokenizer,BertModel
import torch
from sklearn.metrics.pairwise import cosine_similarity
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    words = word_tokenize(text)
    words = [word for word in words if word not in stopwords.words('english')]
    return ' '.join(words)
df['Processed Statement']=df['problem statement title'].apply(preprocess_text)
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')
def get_bert_embedding(text):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()

df['Embedding'] = df['Processed Statement'].apply(get_bert_embedding)
def rank_problem_statements(query):
    query_processed = preprocess_text(query)
    query_embedding = get_bert_embedding(query_processed)
    similarities = df['Embedding'].apply(lambda x: cosine_similarity([query_embedding], [x]).flatten()[0])
    ranked_indices = similarities.argsort()[::-1]
    return df.iloc[ranked_indices]['S.NO.'].tolist()
query = "I need someone who has worked on AI related chatbot in healthcare"
ranked_serial_numbers = rank_problem_statements(query)
print(ranked_serial_numbers)