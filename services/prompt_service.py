


async def format_prompt( query: str, chunks: list, history: list = [None] ) -> str:
    formatted_history = "No previous conversation."

    if history:

        history_lines = []

        for message in history:

            role = message.get("role", "unknown").capitalize()
            content = message.get("content", "")

            history_lines.append(
                f"{role}: {content}"
            )

        formatted_history = "\n".join(history_lines)


    formatted_chunks = "No relevant context retrieved."

    if chunks:

        chunk_lines = []

        for i, chunk in enumerate(chunks):

            chunk_content = chunk.get("content", "")

            chunk_lines.append(f""" Chunk {i + 1}:{chunk_content} """)

        formatted_chunks = "\n".join(chunk_lines)


    final_prompt = f"""
        You are Recall.ai, an intelligent personal knowledge copilot.

        Your responsibilities:
        - Answer questions using the retrieved document context.
        - Use conversation history for continuity.
        - If answer is not present in retrieved context, clearly say so.
        - Do NOT hallucinate or invent information.
        - Keep answers clear, structured, and relevant.
        - Prefer retrieved context over assumptions.

        ==================================================
        CONVERSATION HISTORY
        ==================================================

        {formatted_history}

        ==================================================
        RETRIEVED DOCUMENT CONTEXT
        ==================================================

        {formatted_chunks}

        ==================================================
        CURRENT USER QUESTION
        ==================================================

        {query}

        ==================================================
        INSTRUCTIONS
        ==================================================

        - Answer the CURRENT USER QUESTION.
        - Use conversation history only for contextual continuity.
        - Use retrieved document chunks as primary knowledge source.
        - If retrieved context is insufficient, explicitly mention it.
        """

    return final_prompt.strip()