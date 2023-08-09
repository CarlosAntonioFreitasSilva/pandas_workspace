from sqlalchemy.orm import Session
from alchemy.models import Contato


# create CRUDS methods

def insert_contato(session : Session, contact: Contato):
    new_contact = Contato(nome=contact.nome,celular=contact.celular)
    session .add(new_contact)
    session.commit()
    session.refresh(new_contact)
    return new_contact

def get_contatos(session: Session):
    return session.query(Contato).all()

def update_contato(session: Session, contact: Contato):
    return session.query(Contato).filter(Contato.nome == contact.nome)

def delete_contato(session: Session, contact: Contato):
    return session.query(Contato).filter(Contato.celular == contact.celular).delete()

# from sqlalchemy import select
# stmt = select(User).where(User.name == "spongebob")
# session.execute(stmt)