import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
df = pd.read_csv('csvforgemini.csv')
# nltk.download('punkt')
# nltk.download('stopwords')
def preprocess_text(text):
    text = text.lower()
    # Remove punctuation and special characters
    text = re.sub(r'\W', ' ', text)
    # Tokenizati0n
    words = word_tokenize(text)
    # Removal of stop word
    words = [word for word in words if word not in stopwords.words('english')]
    return ' '.join(words)

df['Processed Statement'] = df['problem statement title'].apply(preprocess_text)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
vectorizer=TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['Processed Statement'])
def rank_problem_statements(query):
   
    query_processed = preprocess_text(query)
    
    query_vec = vectorizer.transform([query_processed])
   
    cosine_similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
    
    ranked_indices = cosine_similarities.argsort()[::-1]
    
    return df.iloc[ranked_indices]['S.NO.'].tolist()
query = "AI chatbot in healthcare"
ranked_serial_numbers = rank_problem_statements(query)
print(ranked_serial_numbers)