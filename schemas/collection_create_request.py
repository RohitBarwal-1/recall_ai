from pydantic import BaseModel
from typing import Optional


class CollectionCreateRequest(BaseModel):
    user_id: str
    collection_name: str
    collection_description: Optional[str]
    collection_settings: Optional[dict]