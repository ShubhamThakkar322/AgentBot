import os
import streamlit as st 
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate


load_dotenv()
GEMINI_KEY = os.environ.get("GEMINI_API_KEY")
CHROMA_DB_DIR = "chroma_db_rag"
RAG_MODEL = "gemini-2.5-flash"

RAG_PROMPT_TEMPLATE = """
You are an expert AI assistant that answers questions based ONLY on the provided context.
If the answer is not found in the context, clearly state: "I cannot answer this based on the provided project information."

Context: {context}
Question: {question}
"""

@st.cache_resource 
def setup_rag_chain():
    """
    Sets up and returns the complete Retrieval-Augmented Generation chain.
    """
   
    embeddings = GoogleGenerativeAIEmbeddings(
        model="text-embedding-004", 
        google_api_key=GEMINI_KEY
    )
    
    vectorstore = Chroma(
        persist_directory=CHROMA_DB_DIR, 
        embedding_function=embeddings
    )

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 2} 
    )
    
    llm = ChatGoogleGenerativeAI(
        model=RAG_MODEL,
        temperature=0.1, 
        google_api_key=GEMINI_KEY 
    )
    
    rag_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff", 
        retriever=retriever,
        return_source_documents=False,
        chain_type_kwargs={
            "prompt": PromptTemplate.from_template(RAG_PROMPT_TEMPLATE)
        }
    )
    
    return rag_chain

rag_chain = setup_rag_chain()
