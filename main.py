from contextlib import asynccontextmanager
from fastapi import FastAPI
from api.router import router
from logging_config import logger




@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Initiating Recall AI ...")

    yield

    logger.info("Recall AI completed its job, going to sleep. Good Bye!")


app = FastAPI(lifespan=lifespan)


app.include_router(router)