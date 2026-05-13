import tempfile
from logging_config import logger
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader, BSHTMLLoader
from fastapi.responses import JSONResponse
from fastapi import status
from .chunking_service import ChunkingService
from .embedding_service import EmbeddingService
from repository.document_chunk_repo import EmbeddingsRepository

async def upload_document_service(data, file):
    logger.info("Document extraction initiated")
    chunking_service = ChunkingService()
    embedding_service = EmbeddingService()
    embeddings_repo  = EmbeddingsRepository()

    file_extension = file.filename.split(".")[-1]
    with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=f".{file_extension}"
        ) as temp_file:

            content = await file.read()
            temp_file.write(content)

            file_path = temp_file.name

    if file_extension == "pdf":
        loader = PyPDFLoader(file_path)

    elif file_extension == "docs":
        loader = Docx2txtLoader(file_path)

    elif file_extension in ["md", "txt"]:
        loader = TextLoader(file_path)

    elif file_extension == "html":
        loader = BSHTMLLoader(file_path)
    
    else:
        return JSONResponse(status_code = status.HTTP_422_UNPROCESSABLE_CONTENT,
                             content = {"message": "unsupported file format"}
                            )
    
    documents = loader.load()

    chunks = await chunking_service.create_recursive_chunks(documents=documents)
    
    chunk_texts = [ chunk.page_content for chunk in chunks ]

    embeddings = await embedding_service.create_embeddings(chunk_texts)

    await embeddings_repo.save_chunks(file.filename, chunks, embeddings)

    logger.info("Document extracion completed successfully")
    return JSONResponse(status_code=status.HTTP_200_OK,
                         content={"message": "Document uploaded successfully"}
                        )   






