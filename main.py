from fastapi import FastAPI, Query
from pydantic import BaseModel
from utils import load_data, get_top_k_recommendations

app = FastAPI()
data = load_data()

class QueryInput(BaseModel):
    query: str
    top_k: int = 10

@app.post("/recommend")
def recommend_assessments(input: QueryInput):
    results = get_top_k_recommendations(input.query, data, input.top_k)
    output = results[[
        'Name', 'URL', 'Remote Support', 'Adaptive Support', 'Duration', 'Test Type'
    ]].to_dict(orient="records")
    return {"recommendations": output}
