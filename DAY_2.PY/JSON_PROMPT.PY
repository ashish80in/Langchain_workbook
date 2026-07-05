from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model=ChatMistralAI(model="mistral-small-2503")

prompt=ChatPromptTemplate.from_messages([
    (
        "system",
        """
Return the answer ONLY as JSON.

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

chain=prompt|model

question=input("Topic: ")

response=chain.invoke({
    "topic":question
})

print(response.content)