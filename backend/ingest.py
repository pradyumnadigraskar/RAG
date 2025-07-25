import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader  
from langchain.text_splitter import RecursiveCharacterTextSplitter

os.environ["GOOGLE_API_KEY"] = "AIzaSyDAefyyevUNKa7klQ7GhmVDIH6CzmH9blY"
embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")



def ingest_pdf_file(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()  

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    docs = text_splitter.split_documents(documents)

    persist_directory = "./chroma_db"
    vectordb = Chroma.from_documents(
        docs, 
        embedding, 
        persist_directory=persist_directory
    )
    variable = "✅ embeded new pdf file to the vector db"
    return(variable)