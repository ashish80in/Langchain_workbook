from langchain_community.document_loaders import TextLoader

loader = TextLoader("your sample txt path")

docs = loader.load()

for doc in docs:
    print(doc.page_content)
    print(doc.metadata)