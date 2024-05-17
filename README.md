# MongodbBounty
### Interactive Learning Assistant with Vector Search

#### Overview

This project implements an Interactive Learning Assistant that leverages MongoDB Atlas Vector Search and LlamaIndex to provide detailed explanations or answers to user queries on various topics. The tool is specifically adapted for urban geography and biology by uploading vectorized documents related to these fields into a MongoDB database. The assistant uses these vectors to retrieve relevant educational content, providing tailored responses to the user's specific questions or learning style.

#### Key Features

- **GPU Acceleration**: Utilizes CUDA-enabled GPUs for faster computation, if available.
- **MongoDB Atlas Vector Search**: Efficiently retrieves relevant documents based on vector similarity.
- **LlamaIndex Integration**: Uses advanced language models from LlamaIndex for generating responses.
- **Streamlit Interface**: Provides a user-friendly web interface for querying and receiving responses.

#### Technology Stack

- **Python**: Core programming language.
- **PyTorch**: For GPU computation and deep learning model integration.
- **MongoDB Atlas**: For database and vector search capabilities.
- **LlamaIndex**: For embedding and language model services.
- **Streamlit**: For creating an interactive web application.

#### How It Works

1. **Vectorization of Documents**: Documents related to urban geography and biology are vectorized using the HuggingFace embedding model.
2. **Storage in MongoDB Atlas**: These vectors are stored in a MongoDB collection, allowing efficient retrieval based on vector similarity.
3. **Query Processing**: User queries are processed using LlamaIndex, which leverages the stored vectors to find the most relevant content.
4. **Response Generation**: The language model generates detailed and tailored responses based on the retrieved content.

#### Setup Instructions

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

#### Example Usage

1. Open the Streamlit application.
2. Enter a query related to urban geography or biology in the text input field.
3. Click the "Submit" button.
4. The assistant will retrieve relevant documents from the MongoDB database and generate a detailed response based on the query.

#### Requirements

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

#### Conclusion

This Interactive Learning Assistant demonstrates the powerful combination of MongoDB Atlas Vector Search and advanced language models to provide tailored educational content. It showcases how modern AI and database technologies can be integrated to create an effective learning tool.

Feel free to contribute to the project or suggest improvements by opening an issue or submitting a pull request.
