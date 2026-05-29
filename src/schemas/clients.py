from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from .base import Base
from datetime import date


#Клиенты
class Clients(Base):

    __tablename__ = "clients"

    client_id: Mapped[int] = mapped_column(primary_key=True)
    last_name: Mapped[str] = mapped_column(String(100))
    first_name: Mapped[str] = mapped_column(String(100))
    phone: Mapped[str] = mapped_column(String(20))
    birthday: Mapped[date]
    registration_day: Mapped[date]