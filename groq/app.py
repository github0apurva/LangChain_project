import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
import time
#set the env values just outside of virtual environment
custom_env_path = lambda a : '/'.join(os.get_exec_path()[0].split('\\')[:-2])+'/'+a
load_dotenv(custom_env_path('chatter.env'))

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

if "vector" not in st.session_state:
    st.session_state.embeddings = OllamaEmbeddings()
    st.session_state.loader = WebBaseLoader("https://docs.smith.langchain.com/")
    st.session_state.docs = st.session_state.loader.load()
    st.session_state.text_splitters = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap=20)
    st.session_state.documents = st.session_state.text_splitters.split_documents(st.session_state.docs[:10] )
    st.session_state.vectors = FAISS.from_documents(st.session_state.documents, st.session_state.embeddings  )

st.title("ChatGroq Demo")
llm = ChatGroq(groq_api_key = os.environ["GROQ_API_KEY"],
               model_name = "llama3-8b-8192" )

prompt = ChatPromptTemplate.from_template(
    """
Answer the questions based on the provided context only.
Please provide the most accurate response based on the question
<context>
{context}
<context>
Questions: {input}
""")


document_chain = create_stuff_documents_chain(llm, prompt)
retriever = st.session_state.vectors.as_retriever()
retrieval_chain = create_retrieval_chain (retriever, document_chain)

prompt = st.text_input ("Input your prompt here ")

if prompt:
    start_time = time.process_time()
    response = retrieval_chain.invoke ({"input":prompt})
    print ("response time: ",time.process_time()-start_time)
    st.write(response['answer'])


    # With a streamlit expander
    with st.expander("Document Similarity Search"):
        # Find the relevant chunks
        for i, doc in enumerate(response["context"]):
            st.write(doc.page_content)
            st.write("--------------------------------")

                                       

