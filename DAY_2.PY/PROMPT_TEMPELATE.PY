# REQUIREMNETS.TXT

# langchain
# langchain-core
# langchain-mistralai
# python-dotenv


from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatMistralAI(model="mistral-small-2503")

prompt = PromptTemplate.from_template(
    "Explain {topic} in simple language."
)

question = input("Enter Topic: ")

final_prompt = prompt.invoke(
    {"topic": question}
)

response = model.invoke(final_prompt)

print(response.content)