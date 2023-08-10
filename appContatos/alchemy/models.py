from alchemy.declarativebase import Base
from sqlalchemy import Column, String, Integer

class Contato(Base):
    __tablename__ = "contatos"
    nome = Column(String)
    celular = Column(String, primary_key=True)
