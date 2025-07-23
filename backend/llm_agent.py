import os
import requests
from dotenv import load_dotenv

# Load API key
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
print("Loaded API Key:", GEMINI_API_KEY)

def generate_sql(question: str) -> str:
    if not GEMINI_API_KEY:
        return "SELECT 'Missing Gemini API key.';"

    prompt = (
        "You are an AI SQL assistant. Given a user question, convert it into an accurate SQLite SQL query.\n"
        "Use the following schema:\n\n"
        "1. total_sales_metrics(date TEXT, item_id INTEGER, total_sales REAL, total_units_ordered INTEGER)\n"
        "2. ad_sales_metrics(date TEXT, item_id INTEGER, ad_sales REAL, impressions INTEGER, ad_spend REAL, clicks INTEGER, units_sold INTEGER)\n"
        "3. eligibility_table(eligibility_datetime_utc TEXT, item_id INTEGER, eligibility INTEGER, message TEXT)\n\n"
        "Rules:\n"
        "- Use only the above columns.\n"
        "- Follow valid SQLite syntax.\n"
        "- Return only the raw SQL query. No markdown, no explanation.\n\n"
        f"Question: {question}"
    )

    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": GEMINI_API_KEY
    }

    data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        raw_text = response.json()['candidates'][0]['content']['parts'][0]['text']
        cleaned_sql = raw_text.strip()

        # Strip common wrappers
        for prefix in ['sqlite>', 'sql', '```sql', '```']:
            if cleaned_sql.lower().startswith(prefix):
                cleaned_sql = cleaned_sql[len(prefix):].strip()
        if cleaned_sql.endswith("```"):
            cleaned_sql = cleaned_sql[:-3].strip()

        # Cleanup tokens
        cleaned_sql = cleaned_sql.replace('ite', '').replace('m_id', 'item_id')

        print("Generated SQL:", cleaned_sql)
        return cleaned_sql

    except Exception as e:
        print(" SQL Generation Error:", e)
        return "SELECT 'Unable to generate SQL due to error.';"


def generate_answer(question: str, result: str) -> str:
    if not GEMINI_API_KEY:
        return " Gemini API key not found."

    prompt = (
        "You are a business data assistant. Based on the user's question and the SQL result (in JSON), "
        "generate a **bold summary sentence** for business users.\n\n"
        f"Question: {question}\n"
        f"SQL Result: {result}\n\n"
        "Return only the natural language answer, do not include extra text."
    )

    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": GEMINI_API_KEY,
    }

    data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        text = response.json()["candidates"][0]["content"]["parts"][0]["text"]
        return text.strip() if text.strip() else " No answer generated."
    except Exception as e:
        print(" LLM Answer Generation Error:", e)
        return "Unable to generate answer."
