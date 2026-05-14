


async def format_prompt(prompt: str, chunks: list) -> str:
    """
    Format the prompt with the retrieved chunks.
    """
    formatted_chunks = "\n\n".join([f"Chunk {i+1}:\n{chunk['content']}" for i, chunk in enumerate(chunks)])
    formatted_prompt = f"{prompt}\n\nRelevant Information:\n{formatted_chunks}"
    return formatted_prompt