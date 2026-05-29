import uvicorn
from fastapi import FastAPI
from config.database.db_helper import db_helper
import asyncio
from fastapi.middleware.cors import CORSMiddleware
from src.routers import get_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:5173"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

app.include_router(get_router())


@app.on_event("startup")
async def startup():
    await db_helper.check_connection()


if __name__ == "__main__":
    uvicorn.run("main:app", host = "0.0.0.0", reload=True)