import os
from langchain_ollama import ChatOllama
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
llm = ChatOllama(model="llama3.2")

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

BASE_DIR = os.path.dirname(__file__)

db = Chroma(
    persist_directory=os.path.join(
        BASE_DIR,
        "chroma_db"
    ),
    embedding_function=embedding
)


def ask_rag(question):

    docs = db.similarity_search(
        question,
        k=3

    )
    print("\nDEBUG DOCUMENTS:\n")
    docs = db.similarity_search(
        question,
        k=3
    )
    for doc in docs:
        print(doc.page_content)
        print("-" * 50)
    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = f"""
Answer ONLY using the provided context.

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content
