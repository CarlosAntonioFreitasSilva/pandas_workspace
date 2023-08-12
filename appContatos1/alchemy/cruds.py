from alchemy import session
from alchemy.models import Contato


# create CRUDS methods

def insert_contato(new_name,new_phone,session = session.my_session):
    new_contact = Contato(nome = new_name,celular = new_phone)
    session .add(new_contact)
    session.commit()
    session.refresh(new_contact)
    

def get_contatos(session = session.my_session):
    contacts = session.query(Contato).all() 
    return contacts


def update_contato(nome,celular,key,session = session.my_session):
    # implementar a verificação se o novo celular já existe
    if (celular == key):
        session.query(Contato).filter(Contato.celular == key).update({"nome":nome})
        session.commit() 
    else:
        session.query(Contato).filter(Contato.celular == key).update({"nome":nome,"celular":celular})
        session.commit()


def delete_contato(celular,session = session.my_session):
    session.query(Contato).filter(Contato.celular == celular).delete()
    session.commit()
