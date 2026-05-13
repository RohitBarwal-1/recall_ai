from utils.model_manager import EmbeddingModel

class EmbeddingService:
    def __init__(self):
        self.embedding_model = EmbeddingModel

    async def create_embeddings(self, chunks):
        embeddings = self.embedding_model.encode(chunks,
                                                 convert_to_tensor=False,
                                                 normalize_embeddings=True
                                                )

        return embeddings.tolist()