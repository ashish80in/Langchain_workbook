#. =====================================requirements.txt===========================================
# 
# 
#  langchain
# langchain-core
# langchain-mistralai
# langchain-ollama
# python-dotenv

# pip install -r requirements.txt

# ===================================.ENV.EXAMPLE==================================================
# MISTRAL_API_KEY=your_mistral_api_key_here

# you can copy it to .env and add their API key.


# =================================CHATBOT.PY===================================================

from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()

model = ChatMistralAI(
    model="YOUR MODEL NAME",
    temperature=0.2
)

question = input("Enter your question: ")

response = model.invoke(question)

print("\nAnswer:\n")
print(response.content)

# ================================CHATBOT_LOOP.PY=============================================
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()

model = ChatMistralAI(
    model="YOUR MODEL NAME"
    temperature=0.2
)

print("Type 'exit' to quit.\n")

while True:

    question = input("You: ")

    if question.lower() == "exit":
        break

    response = model.invoke(question)

    print("Bot:", response.content)

# ============================OLLAMA_CHATBOT.PY=================================================

from langchain_ollama import ChatOllama

model = ChatOllama(
    model="YOUR OLLAMA MODEL "
)

print("Type 'exit' to quit.\n")

while True:

    question = input("You: ")

    if question.lower() == "exit":
        break

    response = model.invoke(question)

    print("Bot:", response.content)