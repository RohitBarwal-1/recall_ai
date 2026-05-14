from .embedding_service import EmbeddingService
from repository.document_chunk_repo import EmbeddingsRepository
from .prompt_service import format_prompt
from .llm_service import call_llm
from fastapi import status
from fastapi.responses import JSONResponse


async def chat_service(payload):
    embedding_service = EmbeddingService()
    embeddings_repo  = EmbeddingsRepository()

    prompt = payload.prompt
    user_id = payload.user_id

    user_query = "query: " + prompt

    user_query_embedding = await embedding_service.create_embeddings(user_query)

    chunks = await embeddings_repo.retrieve_chunks(user_query_embedding)

    final_prompt = await format_prompt(prompt, chunks)

    llm_response = await call_llm(final_prompt)

    return JSONResponse(status_code=status.HTTP_200_OK,
                         content={"message": llm_response}
                        )
