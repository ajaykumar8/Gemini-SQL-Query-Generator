from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Load environment variables
load_dotenv()  # Load all the environment variables

# Configure Genai Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini Model and provide queries as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

# Function to retrieve query from the database
def read_sql_query(sql, db):
    if not sql:  # Check if SQL is empty
        print("Error: SQL query is empty or None.")
        return []
    
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    try:
        cur.execute(sql)
        rows = cur.fetchall()
        conn.commit()
    except sqlite3.Error as e:
        print(f"SQL Error: {e}")
        rows = []
    finally:
        conn.close()
    
    return rows

# Define your prompt
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output
    """
]

# Streamlit App
st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

# If submit is clicked
if submit:
    response = get_gemini_response(question, prompt)  # Pass the prompt correctly
    if response:  # Ensure response is not None or empty
        st.write(f"Generated SQL Query: {response}")  # Log the generated SQL for debugging
        data = read_sql_query(response, "student.db")  # Read data using the generated SQL
        
        st.subheader("The Response is:")
        for row in data:
            st.write(row)  # Display each row of the result
    else:
        st.error("Failed to generate a valid SQL query.")  # Show error if response is invalid
