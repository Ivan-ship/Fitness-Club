from fastapi import APIRouter
from sqlalchemy import select
from config.database.db_helper import db_helper
from src.schemas.client_schema import ClientRead, UpdateClients, ClientCreate
from src.schemas.clients import Clients
from sqlalchemy import update, delete

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

    #Upadte
    @router.put("/clients/{client_id}")
    async def update_client(client_id: int, client: UpdateClients):
        async with db_helper.session_factory() as session:
            smt = (
                update(Clients)
                .where(Clients.client_id == client_id)
                .values(
                    last_name = client.last_name,
                    first_name = client.first_name,
                    phone = client.phone
                    )
            )
            await session.execute(smt)
            await session.commit()
            return {"message": "Update client"}
        
    @router.post("/clients", response_model=ClientRead)
    async def create_client(client: ClientCreate):
        async with db_helper.session_factory() as session:
            new_client = Clients(**client.model_dump())
            session.add(new_client)
            await session.commit()
            await session.refresh(new_client)
            return new_client
    
    #Delete
    @router.delete("/clients/{client_id}")
    async def delete_client(client_id: int):
        async with db_helper.session_factory() as session:
            smt = (
                delete(Clients)
                .where(Clients.client_id == client_id)
            )
            await session.execute(smt)
            await session.commit()
            return{"message": "Delete Client"}
    return router