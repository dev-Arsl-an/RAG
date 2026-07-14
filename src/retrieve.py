from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


def retrieve_documents(query):

    # Same embedding model used while indexing
    embedding_model = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en-v1.5"
    )

    # Load existing Chroma database
    vector_db = Chroma(
        persist_directory="./chroma_db",
        embedding_function=embedding_model
    )

    # Create retriever
    retriever = vector_db.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 5,
            "fetch_k": 20
        }
    )

    # Retrieve relevant documents
    results = retriever.invoke(query)

    return results