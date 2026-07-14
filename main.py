# from src.load_pdf import load_pdf
# from src.chunk_pdf import chunk_documents
# from src.embed_documents import create_vector_db
# from src.retrieve import retrieve_documents
from src.rag_pipeline import ask_rag
# pdf_path="data\\PAKFASAL FYP 1 Document.pdf"
# documents = load_pdf(pdf_path)
# print(f"Loaded {len(documents)} documents from {pdf_path}")

# print(documents[77]) 


# chunks = chunk_documents(documents)
# print("Number of chunks created:", len(chunks))

# vector_db = create_vector_db(chunks)
# print("Vector database created.")

# while True:

#     query = input("\nEnter your query (or type 'exit' to quit): ")

#     if query.lower() == "exit":
#         print("Goodbye!")
#         break

#     results = retrieve_documents(query)

#     for i, doc in enumerate(results, start=1):

#         print("-" * 50)
#         print(f"Result {i}")
#         print(f"Page: {doc.metadata['page'] + 1}")
#         print("Content:")
#         print(doc.page_content)
#         print()


while True:
    query = input("Ask a question (type 'exit' to quit): ")

    if query.lower() == "exit":
        break

    answer = ask_rag(query)

    print("\nAnswer:\n")
    print(answer)
    print()