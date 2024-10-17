import os
from PyPDF2 import PdfReader

from langchain_community.chat_models import ChatOpenAI
from langchain_community.embeddings import OpenAIEmbeddings

from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

from langchain_community.vectorstores import FAISS


from dotenv import load_dotenv

load_dotenv()
    
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")


def get_pdf_text(pdf_docs):
    # Read the PDF files and extract the text into a single string.
    text=""
    for pdf in pdf_docs:
        pdf_reader= PdfReader(pdf)
        for page in pdf_reader.pages:
            text+= page.extract_text()
    return  text



def get_text_chunks(text):
    # Split the text into chunks using a recursive character text splitter.
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
    chunks = text_splitter.split_text(text)
    return chunks



def get_vector_store(text_chunks):
    # Initialize an OpenAI embeddings model and create a FAISS vector store with the text chunks as the documents.
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    return vector_store



def get_conversational_chain(vector_store):
    # Create an OpenAI model and a conversation chain using the vector store as the retriever.
    llm = ChatOpenAI(
        temperature = 0.3,
        model = "gpt-3.5-turbo"
    )

    memory = ConversationBufferMemory(memory_key = "chat_history", return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=vector_store.as_retriever(), memory=memory)
    return conversation_chain