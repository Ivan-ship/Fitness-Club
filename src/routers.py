from fastapi import APIRouter
from sqlalchemy import select
from config.database.db_helper import db_helper
from src.schemas.client_schema import ClientRead
from src.schemas.clients import Clients

def get_router():
    router = APIRouter()

    @router.get("/")
    async def root():
        return  {"message": "Привет от FastApi"}
    
    @router.get("/clients", response_model=list[ClientRead])
    async def get_client():
        async with db_helper.session_factory() as session:
            result = await session.execute(
                select(Clients)
            )

            clients = result.scalars().all()
            return clients
    return router