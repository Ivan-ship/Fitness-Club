import uvicorn
from fastapi import FastAPI
from config.database.db_helper import db_helper
import asyncio

app = FastAPI()

@app.get("/")
def root():
    return  {"message": "Hello World!"}

@app.on_event("startup")
async def startup():
    await db_helper.check_connection()


if __name__ == "__main__":
    uvicorn.run("main:app", host = "0.0.0.0", reload=True)