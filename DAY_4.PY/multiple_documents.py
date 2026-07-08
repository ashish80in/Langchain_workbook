from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyPDFLoader

text_loader = TextLoader("sample.txt path")

pdf_loader = PyPDFLoader("sample.pdf path")

text_docs = text_loader.load()

pdf_docs = pdf_loader.load()

all_docs = text_docs + pdf_docs

print("Total Documents")

print(len(all_docs))