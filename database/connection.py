from sqlalchemy .ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

Base = declarative_base()

DATABASE_URL = "postgresql+asyncpg://postgres:Admin%40123@localhost:5432/postgres"

engine = create_async_engine(DATABASE_URL, 
                             echo=True)

async_session = async_sessionmaker(autocommit=False, 
                                autoflush=False, 
                                bind=engine, 
                                class_=AsyncSession, 
                                expire_on_commit=False
                                )