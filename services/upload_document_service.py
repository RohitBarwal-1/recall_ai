import tempfile
import logging
from fastapi import status
from fastapi.responses import JSONResponse
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader, BSHTMLLoader
from repository.document_chunk_repo import EmbeddingsRepository
from repository.document_repo import DocumentRepository
from services.chunking_service import ChunkingService
from services.embedding_service import EmbeddingService

logger = logging.getLogger(__name__)


async def upload_document_service(data, file):
    logger.info(f"Adding new document for user: {data.user_id}")
    chunking_service = ChunkingService()
    embedding_service = EmbeddingService()
    embeddings_repo  = EmbeddingsRepository()
    document_repo = DocumentRepository()
    await document_repo.add_document(data, file)
    
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






