from langchain_community.document_loaders.csv_loader import CSVLoader

loader = CSVLoader("sample.csv")

docs = loader.load()

for doc in docs:
    print(doc.page_content)