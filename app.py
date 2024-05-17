import os
import torch
import logging
import sys
from dotenv import find_dotenv, dotenv_values
from pymongo import MongoClient
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.replicate import Replicate
from llama_index.core import ServiceContext, StorageContext, VectorStoreIndex
from llama_index.vector_stores.mongodb import MongoDBAtlasVectorSearch
import streamlit as st

# Streamlit UI setup
st.title("Interactive Learning Assistant with Vector Search(with a focus on Urban Geography and Biology)")
st.write("Check if GPU is enabled and initialize MongoDB Atlas connection.")

# Check if GPU is enabled
if torch.cuda.is_available():
    st.success("CUDA/GPU is available!")
    for i in range(torch.cuda.device_count()):
        st.write(f"Device {i}: {torch.cuda.get_device_properties(i).name}")
else:
    st.warning("CUDA/GPU is not available. Using CPU.")

# Setup logging
logging.basicConfig(stream=sys.stdout, level=logging.WARNING)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# Load settings from .env file
config = dotenv_values(find_dotenv())

# MongoDB Atlas URI
ATLAS_URI = st.secrets['ATLAS_URI']



if not ATLAS_URI:
    st.error("'ATLAS_URI' is not set. Please set it in the .env file to continue...")
    st.stop()
else:
    st.write("ATLAS_URI Connection string found:")

# Define our variables
DB_NAME = 'rag1'
COLLECTION_NAME = '10k'
INDEX_NAME = 'idx_embedding1'

# Set llamaindex cache dir to ../cache dir here (Default is system tmp)
os.environ['LLAMA_INDEX_CACHE_DIR'] = os.path.join(os.path.abspath('../'), 'cache')

# Initialize MongoDB client
mongodb_client = MongoClient(ATLAS_URI)
st.write("Atlas client initialized")

# Initialize HuggingFaceEmbedding model
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

# Initialize Replicate model
os.environ["REPLICATE_API_TOKEN"] = st.secrets["REPLICATE_API_TOKEN"]
#os.environ["REPLICATE_API_TOKEN"] = "r8_JKo74VC0fuP9QUX1YBVhifJAXoU2cvI0oZwBT"
llm = Replicate(model="a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5")

# Initialize ServiceContext
service_context = ServiceContext.from_defaults(embed_model=embed_model, llm=llm)

# Initialize MongoDBAtlasVectorSearch
vector_store = MongoDBAtlasVectorSearch(
    mongodb_client=mongodb_client,
    db_name=DB_NAME,
    collection_name=COLLECTION_NAME,
    index_name=INDEX_NAME,
)

# Initialize StorageContext and VectorStoreIndex
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_vector_store(vector_store=vector_store, service_context=service_context)

# Query input and response handling
query = st.text_input("Enter your query:")
if st.button("Submit"):
    if query:
        response = index.as_query_engine().query(query)
        st.markdown("**Response:**")
        st.write(response.response)
    else:
        st.warning("Please enter a query.")
