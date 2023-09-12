# Engine
from sqlalchemy import create_engine
engine = create_engine("sqlite:///./database.db", echo=True)

# Sesssion
from sqlalchemy.orm import Session
session = Session(engine)

# Object Relational Mapping
# Declarative Base
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

# Models
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, String, Integer

class Contato(Base):
    __tablename__ = "contatos"
    nome = Column(String)
    celular = Column(String, primary_key=True)

    def __repr__(self):
        return f"Contato(nome = {self.nome}, celular = {self.celular})"

# CRUDS

session.query(Contato).filter(Contato.celular == "87 9 1234").update({"nome":"Carlos Freitas"})
session.commit()