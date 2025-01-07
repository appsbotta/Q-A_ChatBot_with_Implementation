from langchain.llms import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os
import streamlit as st

## Function to load OpenAI and its output


def get_openaiResponse(question):
    llm = OpenAI(openai_api_key = os.getenv("OPENAI_API_KEY"),model_name="davinci-002",temperature=0.5)
    response = llm(question)
    return response

st.set_page_config(page_title="Q&A Demo")

st.header("LangChain Application")

input = st.text_input("Input: ",key="input")
response = get_openaiResponse(input)


submit = st.button("Ask the question")

if submit:
    st.subheader("The response is ")
    st.write(response)

