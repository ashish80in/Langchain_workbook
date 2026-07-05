from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model=ChatMistralAI(model="mistral-small-2503")

prompt=ChatPromptTemplate.from_messages([
    ("system",
     "You are a funny AI. Add jokes in every answer."),
    ("human",
     "{question}")
])

chain=prompt|model

question=input("Ask: ")

response=chain.invoke({
    "question":question
})

print(response.content)