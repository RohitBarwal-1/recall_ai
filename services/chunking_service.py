from langchain_text_splitters import RecursiveCharacterTextSplitter


class ChunkingService:
    def __init__(self):
        self.recursive_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,
                                                                 chunk_overlap=200
                                                                )
    
    async def create_recursive_chunks(self, documents):
        chunks = self.recursive_splitter.split_documents(documents)

        return chunks