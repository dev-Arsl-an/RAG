from src.retrieve import retrieve_documents
from src.prompt import create_prompt
from src.llm import generate_answer


def ask_rag(query):

    documents = retrieve_documents(query)

    prompt = create_prompt(query, documents)

    answer = generate_answer(prompt)

    return answer