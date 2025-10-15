import os
from dotenv import load_dotenv
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma

GEMINI_KEY = os.environ.get("GEMINI_API_KEY")

if not GEMINI_KEY:
    print("FATAL ERROR: GEMINI_API_KEY not found. Cannot proceed with RAG setup.")
    exit()

FILE_PATH = "project_info.txt"
CHROMA_DB_DIR = "chroma_db_rag"

def create_vector_store():
    """
    Loads a document, splits it into chunks, creates embeddings, 
    and saves them to a Chroma vector store.
    """
    print(f"--- Starting RAG Indexing for {FILE_PATH} ---")

    try:
        loader = TextLoader(FILE_PATH)
        documents = loader.load()
        print(f"Loaded {len(documents)} document(s).")
    except Exception as e:
        print(f"Error loading file: {e}")
        return

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    texts = text_splitter.split_documents(documents)
    print(f"Split into {len(texts)} chunks.")

    embeddings = GoogleGenerativeAIEmbeddings(
        model="text-embedding-004", 
        google_api_key=GEMINI_KEY
    )
    print("Embedding model initialized.")

    vectorstore = Chroma.from_documents(
        documents=texts,
        embedding=embeddings,
        persist_directory=CHROMA_DB_DIR
    )
    vectorstore.persist()
    print(f"Successfully created Vector Store and saved to '{CHROMA_DB_DIR}'")

if __name__ == "__main__":
    create_vector_store()
