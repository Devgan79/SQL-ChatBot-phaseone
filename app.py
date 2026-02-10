from dotenv import load_dotenv
load_dotenv()

#load env

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-flash-lite-latest')
    response=model.generate_content([prompt[0],question])
    return response.text

#fun to read query from sql db 

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

# define promt 

prompt=[
    """
You are an very expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output

"""
]

## Streamlit deployment

st.set_page_config(page_title="Hey im your Sql ChatBot how can i help you")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("input:",key="input")
submit=st.button("Ask the Question")

if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    data=read_sql_query(response,"student.db")
    st.subheader("The Response is ")
    for row in data:
        print(row)
        st.header(row)