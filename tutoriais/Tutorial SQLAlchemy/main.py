from sqlalchemy import create_engine
engine = create_engine("sqlite:///./database.db", echo=True)

from sqlalchemy.orm import Session
session = Session(engine)

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass


from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String


class Contato(Base):
    __tablename__ = "contatos"
    nome : Mapped[str] = mapped_column(String(30))
    celular: Mapped[str] = mapped_column(String(30), primary_key=True)

    def __repr__(self):
        return f"Contato(nome = {self.nome}, celular = {self.celular})"
    
# Base.metadata.create_all(engine)

jose = Contato(nome="José Paulo",celular = "62 9 8976")
carlos = Contato(nome="Carlos Freitas",celular = "78 9 8976")
# session.add(carlos)
# session.add(jose)
# session.commit()


# print(session.get(Contato, "78 9 8976"))

from sqlalchemy import select,update,delete

# print(select(Contato))
# print(session.execute(select(Contato)).all())
# print(session.execute(select(Contato)).first())

stmt = select(Contato)
print(session.execute(stmt).all())


#Selecionando colunas

# print(session.execute(select(Contato.nome)).all())
# print(session.execute(select(Contato.celular)).all())
# print(session.execute(select(Contato.celular)).first())
# print(session.execute(select(Contato.celular).where(Contato.nome == "Carlos Freitas")).all())
# print(session.execute(select(Contato.celular).where(Contato.nome == "Carlos Freitas")).all())
# print(session.execute(select(Contato.celular).where(Contato.nome == "Carlos")).all())
# print(session.execute(select(Contato.celular).filter_by(nome = "Carlos Freitas")).all())
# print(session.execute(select(Contato).order_by(Contato.nome)).all())
# print(session.execute(select(Contato).order_by(Contato.nome.desc())).all())


# Update
# session.execute(update(Contato).where(Contato.nome == "Inacio Paes").values(nome = "Inácio Paes"))
# session.commit()

# Delete

# session.execute(delete(Contato).where(Contato.nome == "Carlos Freitas"))
# session.commit()




new_contato = Contato(nome = "Carlos Freitas",celular = "78 7 8976")
def checkContato(new_contato):
    check = session.get(Contato, new_contato.celular)
    if (check == None):
        session.add(new_contato)
        session.commit()
    else:
        return True

