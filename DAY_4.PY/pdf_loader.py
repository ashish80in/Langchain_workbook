from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("sample.pdf path")

docs = loader.load()

print("Number of pages:",len(docs))

for doc in docs:
    print("="*50)
    print(doc.page_content)


    # Every PDF page becomes one Document.

# Suppose PDF has
# 10 pages
# Then
# Python
# len(docs)
# returns
# 10
