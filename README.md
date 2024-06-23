# LangChain_project
Using langchain 0.2 and the whole system

Steps
1) created a virtual environment
2) installed all the requirements
3) chatbot/app.py: created a python notebook to query openai chat gpt3.5 and logging on langsmith, this use streamlit for webapp
4) chatbot/local_lama.py: doing the same thing using Ollama 
    ( how - a. download ollama & install
            b. windows command propmt 
            c. running "ollama run llama2
    )

5) api/app.py: build an api and added routes using fastapi, hosted at local host 8000
6) api/client.py: client side webapp 
7) execute "python app.py" & "streamlit run client.py" in seperate cmd
8) rag/simplerag.ipynb: being used to load, transform and  Embed to a vector store (used instruct/ollama as openaiembeddings is not openscource )
9) chain
10) agenta
11) groq
100) pushed it to git for now