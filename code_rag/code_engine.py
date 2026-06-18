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

def ask_code(question):

    docs = db.similarity_search(
        question,
        k=4
    )

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = f"""
You are an expert software engineer.

Answer ONLY from the code context.

Code Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content
