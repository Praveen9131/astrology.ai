import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Define Langchain and OpenAI settings
LANGCHAIN_TRACING_V2 = "true"
LANGCHAIN_ENDPOINT = "https://api.smith.langchain.com"
LANGCHAIN_API_KEY = "ls__dd7a651927a04857a7ec44a67fc190c9"
LANGCHAIN_PROJECT = "d68ec6a1-b293-483a-b0e0-1da699282790"

# Initialize Langchain components
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user's request only based on the given context"),
        ("user", "Question: {question}\nContext: {date}")
    ]
)

model = ChatOpenAI(
    model="gpt-3.5-turbo",
    openai_api_key=""
)

output_parser = StrOutputParser()

chain = prompt | model | output_parser

# Streamlit UI
st.title("Astrology Application")


# User input for date of birth
date_of_birth = st.text_input("Enter your date of birth (e.g., April 18, 1990):")

# Button to generate astrology report
if st.button("Generate Astrology Report"):
    # Generate astrology report based on user input
    question = "can you give me astrology based on the date"
    context = f"Date: {date_of_birth}"
    response = chain.invoke({"question": question, "date": context})

    # Display the response
    st.write("Astrology Report:")
    st.write(response)
