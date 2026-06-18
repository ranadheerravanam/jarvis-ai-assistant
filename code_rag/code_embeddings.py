import os

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document

documents = []

for root, dirs, files in os.walk("."):

    dirs[:] = [
        d for d in dirs
        if d not in [
            "venv",
            "__pycache__",
            ".git",
            "chroma_db"
        ]
    ]

    for file in files:

        if file.endswith(".py"):

            path = os.path.join(root, file)

            try:

                with open(
                    path,
                    "r",
                    encoding="utf-8"
                ) as f:

                    content = f.read()

                documents.append(
                    Document(
                        page_content=content,
                        metadata={"source": path}
                    )
                )

            except:
                pass

print("Files Loaded:", len(documents))

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(
    documents
)

print("Chunks:", len(chunks))

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma.from_documents(
    chunks,
    embedding,
    persist_directory="./code_rag/chroma_db"
)

print("Codebase indexed successfully!")
