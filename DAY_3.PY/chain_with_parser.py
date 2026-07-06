from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatMistralAI(model="mistral-small-2503")

prompt = PromptTemplate.from_template(
    "Explain {topic} in simple language."
)

parser = StrOutputParser()

chain = prompt | model | parser

question = input("Topic: ")

response = chain.invoke({
    "topic": question
})

print(response)