from langchain_text_splitters import CharacterTextSplitter

text = "This is a demonstration of chunk overlap in LangChain text splitting."

splitter = CharacterTextSplitter(
    separator=" ",
    chunk_size=25,
    chunk_overlap=10
)

chunks = splitter.split_text(text)
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}: {chunk}")
