from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Load model once
model = SentenceTransformer('all-MiniLM-L6-v2')

def load_data(path='shl_data.csv'):
    df = pd.read_csv(path)
    df['embedding'] = df['Description'].apply(lambda x: model.encode(x))
    return df

def get_top_k_recommendations(query, df, k=10):
    query_embedding = model.encode(query)
    similarities = df['embedding'].apply(lambda x: cosine_similarity([query_embedding], [x])[0][0])
    df['similarity'] = similarities
    return df.sort_values('similarity', ascending=False).head(k)
