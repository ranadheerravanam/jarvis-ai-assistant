from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

pdf = input("PDF Path: ")

loader = PyPDFLoader(pdf)

docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(docs)

print("\nChunks:", len(chunks))

print("\nFirst Chunk:\n")

print(chunks[0].page_content)
