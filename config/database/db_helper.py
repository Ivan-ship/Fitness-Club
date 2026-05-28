from asyncio import current_task
from contextlib import asynccontextmanager #контекстный менеджер
from .db_config import settings_db         
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
    async_scoped_session
)
from sqlalchemy import text



class DataBaseHelper:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(url=url, echo=echo)

        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )
    
    def get_scoped_session(self):
        return async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task
        )
    
    async def check_connection(self):
        try:
            async with self.engine.begin() as conn:
                result = await conn.execute(text("SELECT 1"))
                print("БД подключилась!")
                print(result.scalar())
        except Exception as ex:
            print(f"Ошибка подключения! {ex}")
    

db_helper = DataBaseHelper(
    url=settings_db.database_url,
    echo= settings_db.DB_ECHO_LOGS
)