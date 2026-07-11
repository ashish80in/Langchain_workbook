from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load PDF
loader = PyPDFLoader("sample.pdf")
documents = loader.load()

# Split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
docs = splitter.split_documents(documents)

for i, doc in enumerate(docs[:5]):  # show first 5 chunks
    print(f"Chunk {i+1}:")
    print(doc.page_content)
    print("-" * 40)
