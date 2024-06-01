from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv
#set the env values just outside of virtual environment
custom_env_path = lambda a : '/'.join(os.get_exec_path()[0].split('\\')[:-2])+'/'+a
load_dotenv(custom_env_path('chatter.env'))
from langchain_community.llms import Ollama



## LangSmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")


## prompt template
prompt = ChatPromptTemplate.from_messages(
[
    ("system","You are a helpful assistnat. Please respond to the user queries"),
    ("user","Question:{question}")

]
)


## Streamlit framework
st.title('Langchain Demo with LLAMA2')
input_text = st.text_input("search the topic u want")



## Ollama - LLama2 
llm = Ollama(model = "llama2")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))



