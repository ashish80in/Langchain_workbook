from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatMistralAI(model="mistral-small-2503")

parser = StrOutputParser()

chain = model | parser

question = input("Ask: ")

response = chain.invoke(question)

print(response)