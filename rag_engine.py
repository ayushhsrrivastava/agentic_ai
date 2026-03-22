from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.document_loaders import TextLoader
import os

DB_DIR = "vector_db"

def load_documents():
    docs = []
    for file in os.listdir("data"):
        if file.endswith(".txt"):
            loader = TextLoader(f"data/{file}")
            docs.extend(loader.load())
    return docs

def create_vector_store():
    docs = load_documents()

    # ✅ Use Ollama embeddings (NOT OpenAI)
    embeddings = OllamaEmbeddings(model="llama3")

    db = Chroma.from_documents(
        docs,
        embeddings,
        persist_directory=DB_DIR
    )

    db.persist()
    print("✅ Vector DB created successfully!")
    return db

def get_retriever():
    embeddings = OllamaEmbeddings(model="llama3")

    db = Chroma(
        persist_directory=DB_DIR,
        embedding_function=embeddings
    )

    return db.as_retriever(search_kwargs={"k": 2})