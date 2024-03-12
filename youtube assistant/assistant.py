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

test_url = 'https://www.youtube.com/watch?v=K-nnzpgrzwM'
#Create a vector database with the video transcript
def vector_db_from_youtube(url : str) -> FAISS:

    loader = YoutubeLoader.from_youtube_url(url)
    transcript = loader.load()

    #Split transcript into chunks so that token size is not exceeded
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap = 100)
    docs = text_splitter.split_documents(transcript)

    db = FAISS.from_documents(docs,embeddings)

    return db

def get_response_from_query(db,query,k=4):
    # text davinci has a max token size of 4097 tokens, so we can send 4 docs 
    #since each congtains 1000 tokens. These are the top k documents
    docs = db.similarity_search(query,k=k)
    docs_page_content = " ".join([d.page_content for d in docs])

    llm = OpenAI(model='text-davinci-003')

    prompt = PromptTemplate(

        input_variables = ['query','docs'],

        template = """

        You are a helpful assistant that that can answer questions about youtube videos 
        based on the video's transcript.
        
        Answer the following question: {question}
        By searching the following video transcript: {docs}
        
        Only use the factual information from the transcript to answer the question.
        
        If you feel like you don't have enough information to answer the question, say "I don't know".
        
        Your answers should be verbose and detailed.
     """
    )

    chain = LLMChain(llm=llm, prompt=prompt)

    response = chain.run(question=query, docs=docs_page_content)

    #Alternative:
    #response = chain({'query':query, 'docs':docs_page_content})

    #Helps with removing new line characters and seperates content using whitespace
    response = response.replace("\n","")

    return response