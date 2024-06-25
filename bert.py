import pandas as pd
from sentence_transformers import SentenceTransformer, util
import torch
df = pd.read_csv('csvforgemini.csv')
# this model is a sentence transformer for converting text to embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')\
# conversion
problem_statements = df['problem statement title'].tolist()
embeddings = model.encode(problem_statements, convert_to_tensor=True)

def find_matching_snos(query, df, embeddings, model, top_k=10): 
    # user query to embedding
    query_embedding = model.encode(query, convert_to_tensor=True)
    cosine_scores = util.pytorch_cos_sim(query_embedding, embeddings)[0]
    #top k matches 
    top_results = torch.topk(cosine_scores, k=top_k)
    # serial numbers
    matching_snos = df.iloc[top_results.indices]['S.NO.'].tolist()
    similarity_scores = cosine_scores[top_results.indices].tolist()
    return matching_snos,similarity_scores
query = "Artificial Intelligence projects"
matching_snos,similarity_scores = find_matching_snos(query, df, embeddings, model)
print(matching_snos)
print(similarity_scores)