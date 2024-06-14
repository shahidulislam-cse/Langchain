import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st

# Set the API keys directly
os.environ["OPENAI_API_KEY"] = ""
os.environ["LANGCHAIN_API_KEY"] = ""

# Ensure necessary environment variables are set
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Define the prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries"),
        ("user", "Question: {question}")
    ]
)

# Streamlit framework
st.title('Langchain Demo With LLAMA2 API')
input_text = st.text_input("Search the topic you want")

# Ollama Llama2 LLM
llm = Ollama(model="llama2")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Process the input and display the response
if input_text:
    st.write(chain.invoke({"question": input_text}))
