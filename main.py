import os
import streamlit as st
import pickle
import time

# ✅ Updated imports for LangChain >= 0.2.0
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama

from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter



# No need for OpenAI key anymore
# from dotenv import load_dotenv
# load_dotenv()

# Set Ollama host (only needed if different from default)
os.environ['OLLAMA_HOST'] = 'http://localhost:11434'

# Streamlit UI
st.title("ScrappyTheRobby: News Research Tool 📈")
st.sidebar.title("News Article URLs")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")
file_path = "faiss_store_ollama.pkl"

main_placeholder = st.empty()

# Initialize local LLM via Ollama
llm = Ollama(model="mistral", temperature=0.9)

if process_url_clicked:
    # Load data from URLs
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text("Data Loading... Started ✅")
    data = loader.load()

    # Split text into chunks
    
    text_splitter = RecursiveCharacterTextSplitter(
    separators=['\n\n', '\n', '.', ','],
    chunk_size=512,     # ✅ Reduce from 1000 to 512
    chunk_overlap=50    # ✅ (optional) Add some overlap
    )

    main_placeholder.text("Splitting Text... ✅")
    docs = text_splitter.split_documents(data)

    # Create embeddings using HuggingFace
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(docs, embeddings)

    main_placeholder.text("Building FAISS Vector Index... ✅")
    time.sleep(2)

    # Save the FAISS index locally
    with open(file_path, "wb") as f:
        pickle.dump(vectorstore, f)

# Accept query from user
query = main_placeholder.text_input("Question: ")
if query:
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            vectorstore = pickle.load(f)
            chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())
            result = chain.invoke({"question": query})


            st.header("Answer")
            st.write(result["answer"])

            sources = result.get("sources", "")
            if sources:
                st.subheader("Sources:")
                for src in sources.split("\n"):
                    st.write(src)
