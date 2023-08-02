from sqlalchemy.orm import Session

import models, schemas


def insert_contato(db: Session, contato: schemas.Contato):
    db_contato = models.Contato(nome=contato.nome,celular=contato.celular)
    db.add(db_contato)
    db.commit()
    db.refresh(db_contato)
    return db_contato

def get_contatos(db: Session):
    return db.query(models.Contato).all()

