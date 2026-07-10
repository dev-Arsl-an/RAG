from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_documents(document):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    chunks = text_splitter.split_documents(document)
    return chunks
