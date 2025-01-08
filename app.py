def BasicChatBot():

    #  from langchain.llms import OpenAI
    # from dotenv import load_dotenv
    # load_dotenv()
    # import os
    # import streamlit as st

    # ## Function to load OpenAI and its output


    # def get_openaiResponse(question):
    #     llm = OpenAI(openai_api_key = os.getenv("OPENAI_API_KEY"),model_name="gpt-3.5-turbo-instruct",temperature=0.5)
    #     response = llm(question)
    #     return response

    # st.set_page_config(page_title="Q&A Demo")

    # st.header("LangChain Application")

    # input = st.text_input("Input: ",key="input")
    # response = get_openaiResponse(input)


    # submit = st.button("Ask the question")

    # if submit:
    #     st.subheader("The response is ")
    #     st.write(response)
    pass

import streamlit as st
from langchain.schema import HumanMessage,SystemMessage,AIMessage
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os


st.set_page_config(page_title="Converstaional Q&A ChatBot")
st.header("Hey lets Chat")

load_dotenv()

chatllm = ChatOpenAI(temperature=0.5)

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [
        SystemMessage(content="You are a comedian AI assistant")
    ]

def get_chatResponse(question):
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer = chatllm(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content

input = st.text_input("Input: ",key="input")
response = get_chatResponse(input)


submit = st.button("Ask the question")

if submit:
    st.subheader("The response is ")
    st.write(response)
