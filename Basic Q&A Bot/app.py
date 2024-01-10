# Q&A Chatbot

from langchain.llms import OpenAI
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()  # takes environment variables from .env

# Function to load openai model and get response
def get_openai_response(question):
    llm = OpenAI(openai_api_key=os.getenv("OPEN_API_KEY"), model_name="gpt-3.5-turbo-instruct", temperature=0.6)
    response = llm(question)
    return response

st.set_page_config(page_title="Q&A Demo")

st.header("Pepe's Chatbot")

user_input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

if submit:
    response = get_openai_response(user_input)
    st.subheader("The response is")
    st.write(response)
