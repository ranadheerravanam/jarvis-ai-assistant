from langchain_community.document_loaders import PyPDFLoader

pdf = input("PDF Path: ")

loader = PyPDFLoader(pdf)

docs = loader.load()

print("\nPages Loaded:", len(docs))

for i, page in enumerate(docs):

    print(f"\n===== PAGE {i+1} =====\n")

    print(page.page_content[:1000])
