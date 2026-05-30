from pydantic import BaseModel
from datetime import date


class Mem_type(BaseModel):
    type_id: int
    name: str
    price: int
    duration: int
    model_config = {
        "from_attributes": True
    }