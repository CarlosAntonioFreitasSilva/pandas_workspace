from sqlalchemy import create_engine
engine = create_engine("sqlite:///./contatos.db", echo=True)

from sqlalchemy.orm import Session
session = Session(engine)

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass


from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, Integer, ForeignKey

# class Contato(Base):
#     __tablename__ = "contatos"
#     nome : Mapped[str] = mapped_column(String(30))
#     celular: Mapped[str] = mapped_column(String(30), primary_key=True)

#     def __repr__(self):
#         return f"Contato(nome = {self.nome}, celular = {self.celular})"
    
# Base.metadata.create_all(engine)

# jose = Contato(nome="José Paulo",celular = "62 9 8976")
# carlos = Contato(nome="Carlos Freitas",celular = "78 9 8976")
# session.add(carlos)
# session.add(jose)
# session.commit()

# maria = Contato(nome="Maria", celular = "11 2 2345")
# marcia = Contato(nome="Macia", celular = "78 2 2345")
# ana = Contato(nome="Maria", celular = "11 8 2565")

# session.add_all([maria,marcia,ana])
# session.commit()

# print(session.get(Contato, "78 9 8976"))

from sqlalchemy import select,update,delete, exc

# print(select(Contato))
# print(session.execute(select(Contato)).all())
# print(session.execute(select(Contato)).first())

# stmt = select(Contato)
# print(session.execute(stmt).all())


def teste():
    try:
        session.query(Contato).filter(Contato.nome == "Antônio").update({"celular" : "62 9 8976"})
        session.commit()
        return True
    except:
        return  False

# print(teste())
# print(session.execute(select(Contato.nome)).all())
# print(session.execute(select(Contato.celular)).all())
# print(session.execute(select(Contato.celular)).first())
# print(session.execute(select(Contato.celular).where(Contato.nome == "Carlos Freitas")).all())
# print(session.execute(select(Contato.celular).where(Contato.nome == "Carlos Freitas")).all())
# print(session.execute(select(Contato.celular).filter_by(nome = "Carlos Freitas")).all())
# print(session.execute(select(Contato).order_by(Contato.nome)).all())
# print(session.execute(select(Contato).order_by(Contato.nome.desc())).all())


# Update
# session.execute(update(Contato).where(Contato.nome == "Inacio Paes").values(nome = "Inácio Paes"))
# session.commit()

# Delete

# session.execute(delete(Contato).where(Contato.nome == "Carlos Freitas"))
# session.commit()




# new_contato = Contato(nome = "Carlos Freitas",celular = "78 7 8976")
def checkContato(contato):
    check = session.get(Contato, contato.celular)
    if (check == None):
        return None
    else:
        return True

def checkContatoName(name: str):
    check = session.execute(select(Contato).where(Contato.nome == name)).all() != []
    if(check):
        return True
    else:
        return False

def checkName(model,nome):
    check = session.execute(select(model).where(model.nome == nome)).all() != []
    if(check):
        return True
    else:
        return False
    
def checkCelular(model,celular):
    check = session.execute(select(model).where(model.celular == celular)).all() != []
    if(check):
        return True
    else:
        return False
    
# print(checkName(Contato,"Carlos"))
# print(checkCelular(Contato,"78 7 897"))

def exists(model,field,value):
    exists = session.execute(select(model).where(field == value)).all() != []
    if(exists):
        return True
    else:
        return False

    
# print(exists(Contato,Contato.nome,"Inácio Paes Freitas"))


class Cliente(Base):
    __tablename__ = "clientes"
    id : Mapped[int] = mapped_column(Integer, primary_key = True)
    nome : Mapped[str] = mapped_column(String(30))
    def __repr__(self):
        return f"Cliente(id = {self.id}, nome = {self.nome})"
    
class Contato(Base):
    __tablename__="contatos"
    cliente_id: Mapped[int] = mapped_column(Integer, ForeignKey(Cliente.id), primary_key=True)
    celular: Mapped[str] = mapped_column(String(9))

cliente = Cliente(nome = "Carlos")
session.add(cliente)
session.commit()

session.query(Cliente).all()
