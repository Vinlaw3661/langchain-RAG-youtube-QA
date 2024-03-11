#Allows loading YouTube video using URL
from langchain_community.document_loaders import YoutubeLoader
#Allows splitting long texts into smaller segments to be stored in vector store
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import LLMChain
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores.faiss import FAISS
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

embeddings = OpenAIEmbeddings()

#Create a vector database with the video transcript
def vector_db_from_youtube(url : str) -> FAISS:

    loader = YoutubeLoader.from_youtube_url(url)
    transcript = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap = 100)
    docs = text_splitter.split_documents(transcript)

    db = FAISS.from_documents(docs,embeddings)

    return db
