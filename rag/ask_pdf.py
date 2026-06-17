from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embedding
)

while True:

    question = input("\nQuestion: ")

    if question.lower() == "exit":
        break

    docs = db.similarity_search(
        question,
        k=3
    )

    print("\nRESULTS:\n")

    for i, doc in enumerate(docs):

        print(f"\nChunk {i+1}:\n")

        print(doc.page_content[:500])
