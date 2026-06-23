from configs.configs import DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_NAME, DATABASE_HOST 
from sqlalchemy .ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

Base = declarative_base()

DATABASE_URL = f"postgresql+asyncpg://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:5432/{DATABASE_NAME}"

engine = create_async_engine(DATABASE_URL, 
                             echo=True)

async_session = async_sessionmaker(autocommit=False, 
                                autoflush=False, 
                                bind=engine, 
                                class_=AsyncSession, 
                                expire_on_commit=False
                                )