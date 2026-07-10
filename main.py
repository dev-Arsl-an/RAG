from src.load_pdf import load_pdf
from src.chunk_pdf import chunk_documents
pdf_path="data\\PAKFASAL FYP 1 Document.pdf"
documents = load_pdf(pdf_path)
print(f"Loaded {len(documents)} documents from {pdf_path}")

# print(documents[77]) 


chunks = chunk_documents(documents)
print(chunks[0])