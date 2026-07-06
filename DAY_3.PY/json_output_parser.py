from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = ChatMistralAI(model="mistral-small-2503")

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
Return ONLY valid JSON.

{
    "topic":"",
    "definition":"",
    "advantages":[]
}
"""
    ),
    (
        "human",
        "{topic}"
    )
])

parser = JsonOutputParser()

chain = prompt | model | parser

question = input("Topic: ")

response = chain.invoke({
    "topic": question
})

print(response)