def create_prompt(query, documents):

    context = "\n\n".join([doc.page_content for doc in documents])

    prompt = f"""
You are an AI assistant.

Answer ONLY from the provided context.

If the answer is not present, say:
"I couldn't find the answer in the provided document."

Context:
{context}

Question:
{query}

Answer:
"""

    return prompt