from langchain_community.document_loaders import PyPDFLoader

def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()  
    return documents

# Each document has 2 things
#    1) Page Content
#     2) Metadata