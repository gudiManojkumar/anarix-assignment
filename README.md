AI-Powered SQL Assistant for E-commerce
This project is a smart SQL assistant for non-technical users to query an e-commerce database using natural language. It uses Gemini LLM to convert questions to SQL, executes them on an SQLite database, and optionally returns chart visualizations using Matplotlib.

🧩 Tech Stack Overview
⚙️ Backend
FastAPI: Builds lightweight and fast RESTful APIs.
Gemini LLM API: Converts natural questions to SQL and explains results in plain English.
SQLite: Local relational database used for storing e-commerce data.

🎨 Frontend
HTML + CSS: Simple and responsive layout.
JavaScript : Handles dynamic form submission and DOM updates using Fetch API.

🗂️ Project Structure

ecommerce/
├── backend/
│   ├── data_load.py           # CSV to DB loader (optional)
│   ├── llm_agent.py           # LLM integration: SQL and answer generation
│   ├── main.py                # FastAPI server
│   ├── models.sql             # SQL schema definition
│   ├── query_engine.py        # Executes SQL queries
├── datasets/                  # Raw data files
│   ├── ad_sales.csv
│   ├── eligibility.csv
│   └── total_sales.csv
├── .env                       # GEMINI_API_KEY here
├── ecommerce.db               # Preloaded SQLite database
├── index.html                 # Main frontend page
├── styles.css                 # Styling for UI
├── requirements.txt           # Python dependencies
├── Pipfile / Pipfile.lock     # Optional pipenv support

Features
1.Ask questions like “What are total sales?”
2.Automatically generates SQL queries using Gemini.
3.Executes SQL and returns a JSON result.
4.Converts result to a human-readable sentence.
5.Clean and user-friendly frontend interface.
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/a7686932-6465-40c6-93b9-099d0594d3b1" />
<img width="1919" height="1012" alt="image" src="https://github.com/user-attachments/assets/05eb52eb-1495-43da-a4bc-c3a1bd83946e" />
<img width="1919" height="1072" alt="image" src="https://github.com/user-attachments/assets/bd0ab7b2-a4ec-43ba-bc32-6b82158a227a" />
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/531f5bae-12d3-4a56-aa24-40c4d75987ec" />
<img width="1919" height="868" alt="image" src="https://github.com/user-attachments/assets/a9d93c01-f07b-42a8-ab89-d8e67a8c8089" />
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/fe747efe-61e3-451a-9b4b-adead17a1654" />





