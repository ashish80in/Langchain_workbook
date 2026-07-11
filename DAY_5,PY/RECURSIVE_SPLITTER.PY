from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """LangChain provides RecursiveCharacterTextSplitter which tries larger separators first 
and falls back to smaller ones if needed."""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=10,
    separators=["\n\n", "\n", " ", ""]
)

chunks = splitter.split_text(text)
print(chunks)
