from pydantic import BaseModel

class Contato(BaseModel):
    nome: str
    celular: str

    class Config:
        orm_mode = True
