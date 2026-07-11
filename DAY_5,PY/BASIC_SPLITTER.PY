from langchain_text_splitters import CharacterTextSplitter

text = "LangChain makes it easy to work with long documents by splitting them into chunks."

splitter = CharacterTextSplitter(
    separator=" ",
    chunk_size=20,
    chunk_overlap=0
)

chunks = splitter.split_text(text)
print(chunks)
