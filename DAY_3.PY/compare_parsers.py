from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatMistralAI(model="mistral-small-2503")

response = model.invoke("What is Machine Learning?")

print("Without Parser:\n")
print(response)
print(type(response))

print("\n----------------------\n")

parser = StrOutputParser()

chain = model | parser

response = chain.invoke("What is Machine Learning?")

print("With StrOutputParser:\n")
print(response)
print(type(response))