import sqlite3
import pandas as pd
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

conn = sqlite3.connect("../staff.db")
cur = conn.cursor()

sql_query = "SELECT name, role, email, department, manager FROM staff"

df = pd.read_sql_query(sql_query, conn)


cur.execute(sql_query)

rows = cur.fetchall()

print(df)

print("\n")
print("="*50)
print("\n")

api_key = os.environ["GROQ_API_KEY"]
groq_base_url = os.environ["GROQ_BASE_URL"]
groq_model = os.environ["GROQ_MODEL"]

client = OpenAI(
    api_key=api_key,
    base_url=groq_base_url
)

history = []


while True: 

    user_input = input("How can I help you today?: ")

    if user_input == "":
        break

    history.append({
        "role": "user",
        "content": f"""
                You're an HR assistant for Leptons Multiconcept Limited in Abuja and you have access to the empoloyees data: 
                <data>{rows}</data>. 
                Provide help to the user based on these information.
                {user_input}"""    
        })
    

    response = client.responses.create(
        model=groq_model,
        input=history
    )

    output_data = response.output_text
    
    history.append({
        "role": "assistant",
        "content": output_data
    })

    print("="*10)
    print(output_data)
    print("="*10)