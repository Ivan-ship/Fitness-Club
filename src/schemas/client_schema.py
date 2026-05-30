from pydantic import BaseModel
from datetime import date

class ClientRead(BaseModel):
    client_id: int
    last_name: str
    first_name: str
    phone: str
    birthday: date
    registration_day: date
    model_config = {
        "from_attributes": True
    }

#Обновление
class UpdateClients(BaseModel):
    last_name: str
    first_name: str
    phone: str

class ClientCreate(BaseModel):
    last_name: str
    first_name: str
    phone: str
    birthday: date
    registration_day: date