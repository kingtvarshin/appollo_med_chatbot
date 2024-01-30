from dotenv import dotenv_values
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import CharacterTextSplitter

config = dotenv_values(".env") 
RAW_DATA_PATH = config["RAW_DATA_PATH"]
VECTOR_DB_PATH = config["VECTOR_DB_PATH"]

def vector_db_creation():
    
    # pdf files loader
    loader = PyPDFDirectoryLoader(path=RAW_DATA_PATH)
    documents = loader.load()
    # text splitter
    text_splitter = CharacterTextSplitter(chunk_size=1000,chunk_overlap=0)
    docs = text_splitter.split_documents(documents)
    # embeddings

# # import
# from langchain_community.embeddings.sentence_transformer import (
#     SentenceTransformerEmbeddings,
# )
# from langchain_community.vectorstores import Chroma

# # create the open-source embedding function
# embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# # load it into Chroma
# db = Chroma.from_documents(docs, embedding_function)

# # query it
# query = "What did the president say about Ketanji Brown Jackson"
# docs = db.similarity_search(query)

# # print results
# print(docs[0].page_content)