import logging
from fastapi import status
from fastapi.responses import JSONResponse
from schemas.collection_create_request import CollectionCreateRequest
from repository.collection_repo import CollectionRepo

logger = logging.getLogger(__name__)


async def collection_create_service(data: CollectionCreateRequest):
    collection_repo = CollectionRepo()
    logger.info(f"Starting collection creation request for user id: {data.user_id}")
    result = await collection_repo.create_collection(data)
    logger.info(f"Collection created successfully")
    return JSONResponse(status_code = status.HTTP_200_OK,
                        content={"collection_id": str(result)})