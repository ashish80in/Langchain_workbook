from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatMistralAI(model="mistral-small-2503")

prompt = ChatPromptTemplate.from_messages([
    ("system","You are an AI Teacher."),
    ("human","{question}")
])

question = input("Enter Question: ")

chain = prompt | model

response = chain.invoke({
    "question":question
})

print(response.content)