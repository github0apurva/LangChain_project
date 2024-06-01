# using fastapi

from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes

import uvicorn 
import os

from langchain_community.llms import Ollama


from dotenv import load_dotenv
#set the env values just outside of virtual environment
custom_env_path = lambda a : '/'.join(os.get_exec_path()[0].split('\\')[:-2])+'/'+a
load_dotenv(custom_env_path('chatter.env'))

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
## LangSmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")


app = FastAPI(
    title ="Langchain Server",
    version="1.0",
    description = "A simple API Server"
)

add_routes(
    app,
    ChatOpenAI(),
    path = "/openai"
)

model_chat= ChatOpenAI()
model_lama=Ollama(model = 'llama2')

prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 10 words")
prompt2 = ChatPromptTemplate.from_template("Write me a poem about {topic} with 10 words")

add_routes(
    app,
    prompt1|model_chat,
    path="/essay"
)

add_routes(
    app,
    prompt2|model_lama,
    path="/poem"
)


if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=8000)