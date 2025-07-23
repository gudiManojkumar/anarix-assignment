import sqlite3

def execute_sql(query: str):
    conn = sqlite3.connect("ecommerce.db")
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    conn.close()
    return [dict(zip(columns, row)) for row in rows]
