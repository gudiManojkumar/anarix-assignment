from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.llm_agent import generate_sql, generate_answer
from backend.query_engine import execute_sql
import json

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    query: str

@app.post("/ask")
def ask_question(question: Question):
    sql_query = generate_sql(question.query)
    result = execute_sql(sql_query)

    try:
        result_str = json.dumps(result)  
    except:
        result_str = str(result)

    answer = generate_answer(question.query, result_str)

    return {
        "original_question": question.query,
        "sql_query": sql_query,
        "result": result,
        "answer": answer
    }
