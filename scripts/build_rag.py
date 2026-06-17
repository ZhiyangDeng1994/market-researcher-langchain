"""Index PDF/TXT reports into a local Chroma vector database.
Run after adding files to data/reports/.

Usage:  python scripts/build_rag.py
"""
from pathlib import Path
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

REPORTS_DIR = Path("data/reports")
VECTORDB_DIR = Path("data/vectordb")


def build():
    docs = []
    for f in REPORTS_DIR.glob("*.pdf"):
        print(f"  Loading {f.name}...")
        docs.extend(PyPDFLoader(str(f)).load())
    for f in REPORTS_DIR.glob("*.txt"):
        print(f"  Loading {f.name}...")
        docs.extend(TextLoader(str(f)).load())

    if not docs:
        print("No PDF or TXT files found in data/reports/")
        print("Add some reports and run this script again.")
        return

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(docs)
    print(f"  Split into {len(chunks)} chunks")

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    Chroma.from_documents(chunks, embeddings, persist_directory=str(VECTORDB_DIR))
    print(f"  Indexed {len(chunks)} chunks -> {VECTORDB_DIR}/")


if __name__ == "__main__":
    print("Building RAG index...")
    build()
    print("Done.")