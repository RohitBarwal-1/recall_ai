from uuid import UUID
from database.connection import async_session
from database.models.users_model import Users
from schemas.user_signup_request import UserSignupRequest


async def create_one_user(user_data: UserSignupRequest) -> UUID:
    async with async_session() as session:
        user = Users(
            email= user_data.email,
            password= user_data.password
        )
        
        session.add(user)
        await session.commit()
        await session.refresh(user)

        return user.user_id 