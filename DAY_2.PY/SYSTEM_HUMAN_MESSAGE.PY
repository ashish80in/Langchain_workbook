from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatMistralAI(model="mistral-small-2503")

prompt = ChatPromptTemplate.from_messages([
    ("system",
     """
     You are a helpful AI.
     Answer politely.
     """),
    ("human","{query}")
])

chain = prompt | model

question = input("Ask: ")

response = chain.invoke({
    "query":question
})

print(response.content)