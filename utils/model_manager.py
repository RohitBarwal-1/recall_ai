import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

load_dotenv()

EmbeddingModel = SentenceTransformer(
    os.getenv("EMBEDDING_MODEL")
)