from fastapi import APIRouter, Depends, File, UploadFile
from logging_config import logger
from schemas.file_upload_request import FileUploadRequest
from services.upload_document_service import upload_document_service
from typing import Optional

router = APIRouter()

@router.post("/upload/document", tags=["Upload documents"])
async def upload_documents_route(data: FileUploadRequest = Depends(), file: UploadFile = File(...), ):
    logger.info("Document upload initiated")
    return await upload_document_service(data, file)