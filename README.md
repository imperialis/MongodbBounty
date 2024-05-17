# MongodbBounty
# Interactive Learning Assistant with Vector Search

## Overview

### Purpose

The Interactive Learning Assistant is designed to provide detailed and contextually relevant explanations or answers to user queries on various topics, with a specific focus on urban geography and biology. The primary purpose is to leverage advanced AI technologies and efficient database search mechanisms to create an educational tool that can tailor its responses to the user's specific questions or learning style.

### Architecture

The core architecture of the project consists of several key components:

1. **Data Storage and Vector Search**: MongoDB Atlas is used to store vectorized representations of educational documents. This allows efficient retrieval of relevant content based on vector similarity.
2. **Embedding and Language Models**: The project uses the HuggingFace embedding model for vectorizing documents and the LlamaIndex language models for generating responses. These models are integrated through the `llama_index` library.
3. **Compute Infrastructure**: PyTorch is employed for GPU acceleration to ensure fast computations, especially during embedding and response generation.
4. **Web Interface**: Streamlit provides the user interface, allowing users to interact with the assistant through a web application. The interface is designed to be intuitive and user-friendly.

## User Interaction Guide

1. **Launching the Application**: Users can access the application via the Streamlit web interface. Upon launching, the application checks for GPU availability and initializes the MongoDB Atlas connection.
2. **Entering Queries**: Users can enter their questions or topics of interest in a text input field provided on the main interface.
3. **Submitting Queries**: After entering a query, users click the "Submit" button. The application processes the query by retrieving the most relevant documents from the MongoDB database and generating a detailed response using the LlamaIndex language model.
4. **Viewing Responses**: The response is displayed on the interface, providing users with comprehensive explanations or answers based on their query. The responses are designed to be informative and tailored to the user's input.

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/interactive-learning-assistant.git
   cd interactive-learning-assistant
   ```

2. **Install Dependencies**

   Create a virtual environment and install the necessary dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**

   In Streamlit Community Cloud:
   - Go to your Streamlit app dashboard.
   - Add the following secrets in the "Secrets" section:
     ```plaintext
     ATLAS_URI="your_mongodb_atlas_uri"
     REPLICATE_API_TOKEN="your_replicate_api_token"
     ```

4. **Run the Application**

   ```bash
   streamlit run app.py
   ```

5. **Deploy on Streamlit Community Cloud**

   - Push your updated code to your GitHub repository.
   - Go to Streamlit Community Cloud and log in with your GitHub account.
   - Create a new app by selecting your repository and specifying the branch and the `app.py` file.
   - Set up your secrets in the Streamlit app settings.
   - Deploy your app.

## Requirements

```plaintext
streamlit
torch
pymongo
llama-index
replicate
llama-index-llms-huggingface
llama-index-embeddings-huggingface
transformers
```

## Conclusion

This Interactive Learning Assistant demonstrates the powerful combination of MongoDB Atlas Vector Search and advanced language models to provide tailored educational content. It showcases how modern AI and database technologies can be integrated to create an effective learning tool.

Feel free to contribute to the project or suggest improvements by opening an issue or submitting a pull request.
