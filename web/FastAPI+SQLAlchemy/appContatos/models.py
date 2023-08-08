from sqlalchemy import Column, String, Integer

from database import Base


class Contato(Base):
    __tablename__ = "contatos"
    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    nome = Column(String)
    celular = Column(String)


