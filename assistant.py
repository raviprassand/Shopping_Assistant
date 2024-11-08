from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
import sqlite3

load_dotenv()

conn = sqlite3.connect('FullStackSQL.db')
print("Your connection Sqlite DB is successfull")
cursor = conn.cursor()


llm = ChatGroq(
    model="llama-3.1-70b-versatile",  # Specify the model name
    temperature=0.7,             # Set the desired temperature
    max_tokens=150,              # Define the maximum number of tokens
    timeout=10,                  # Set a timeout in seconds
    max_retries=2                # Number of retries in case of errors
)

messages = [
    ("system", "You are a helpful Teaching assistant that helps users to solve their queries"),
    ("human", "Hi")
]

response = llm.invoke(messages)
print(response.content)