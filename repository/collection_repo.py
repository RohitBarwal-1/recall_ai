from database.models.collection_model import Collection
from database.connection import async_session
from schemas.collection_create_request import CollectionCreateRequest

class CollectionRepo:
    def __init__(self):
        self.model = Collection

    async def create_collection(self, collection_data: CollectionCreateRequest):
        async with async_session() as session:
            collection = self.model(
                user_id = collection_data.user_id,
                collection_name = collection_data.collection_name
            )
            session.add(collection)
            await session.commit()
            await session.refresh(collection)

            return collection.collection_id