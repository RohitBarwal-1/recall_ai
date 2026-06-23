from fastapi import status
from fastapi.responses import JSONResponse
from repository.users_repo import create_one_user
from services.auth_service import encrypt_password


async def user_signup_service(data):
    data.password = await encrypt_password(data.password)
    result = await create_one_user(data)
    return JSONResponse(status_code = status.HTTP_200_OK,
                        content={"user_id": str(result)}
                        )

