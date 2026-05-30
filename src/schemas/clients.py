from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
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

#Абонементы
class Memberships(Base):
    __tablename__ = "memberships"

    member_id: Mapped[int] = mapped_column(primary_key=True)
    member_status: Mapped[str] = mapped_column(String(100))
    start_date: Mapped[date]
    end_date: Mapped[date]

    type_id: Mapped[int] = mapped_column(
        ForeignKey("membership_types.type_id")
    )
    client_id: Mapped[int] = mapped_column(
        ForeignKey("clients.client_id")
    )
    client = relationship("Clients")

#Вид абонемента
class MembershiTypes(Base):
    __tablename__ = "membership_types"

    type_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[int]
    duration: Mapped[int]