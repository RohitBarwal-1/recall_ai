from fastapi import APIRouter, Depends, File, UploadFile
from logging_config import logger
from schemas.chat_request import ChatRequest
from schemas.file_upload_request import FileUploadRequest
from schemas.user_signup_request import UserSignupRequest
from services.upload_document_service import upload_document_service
from services.chat_service import chat_service
from services.user_signup_service import user_signup_service

router = APIRouter()

@router.post("/upload/document", tags=["Upload documents"])
async def upload_documents_route(data: FileUploadRequest = Depends(), file: UploadFile = File(...), ):
    logger.info("Document upload initiated")
    return await upload_document_service(data, file)


@router.post("/chat", tags=["query document"])
async def chat_route(data: ChatRequest):
    logger.info("User is quering document")
    return await chat_service(data)

@router.post("/user/signup", tags=["User signup"])
async def user_signup_route(payload: UserSignupRequest):
    logger.info("User signup request received")
    return await user_signup_service(payload)