import logging
from .embedding_service import EmbeddingService
from repository.document_chunk_repo import EmbeddingsRepository
from .prompt_service import format_prompt
from .llm_service import call_llm
from .memory_service import ShortTermMemory
from fastapi import status
from fastapi.responses import JSONResponse

logger = logging.getLogger(__name__)

stm = ShortTermMemory()

async def chat_service(payload):
    embedding_service = EmbeddingService()
    embeddings_repo  = EmbeddingsRepository()

    prompt = payload.prompt
    user_id = payload.user_id
    session_id = payload.session_id

    logger.info(f"User Prompt: {prompt}")


    if not session_id:
        session_id = stm.create_session()

        logger.info(f"New session created: {session_id}")

    else:
        logger.info(f"Using existing session: {session_id}")

    history = stm.get_history(session_id)
    logger.info(f"History message count: {len(history)}")
    
    history_text = ""

    for message in history:

        role = message["role"]
        content = message["content"]

        history_text += f"{role}: {content}\n"

    retrieval_query = f"""
                        Conversation History:{history_text}
                        Current User Question:{prompt}
                    """
    
    logger.info("Generating embeddings for retrieval query")
    user_query_embedding = await embedding_service.create_embeddings(retrieval_query)

    logger.info("Retrieving relevant chunks")
    chunks = await embeddings_repo.retrieve_chunks(user_query_embedding)

    logger.info(f"Retrieved chunks count: {len(chunks)}")

    final_prompt = await format_prompt(query=prompt, chunks=chunks, history=history)
    logger.info(f"\n \n Final promt:    {final_prompt} \n \n ")
    logger.info("Calling LLM")
    llm_response = await call_llm(final_prompt)

    logger.info("LLM response generated successfully")

    stm.add_message(session_id=session_id, role="user", content=prompt )

    stm.add_message(session_id=session_id, role="assistant", content=llm_response )
    logger.info("Conversation stored in STM")

    return JSONResponse(status_code=status.HTTP_200_OK,
                         content={"message": llm_response, 
                                  "session_id": session_id
                                  }
                        )
