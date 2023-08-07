# SQL Alchemy - Tutorial
## Engine
Já com o banco de dados criado, chamado `database`,  no diretório do projeto vamos criar o engine.
~~~python
from sqlalchemy import create_engine
engine = create_engine("sqlite:///./database.db", echo=True)
~~~

## Sessões
~~~python
from sqlalchemy.orm import Session
session = Session(engine)
~~~

## Executando SQL
Podemos executar comandos SQL com o método `execute`

~~~python
from sqlalchemy import text

connection = engine.connect()
connection.execute(text('CREATE TABLE contatos (id INTEGER PRIMARY KEY NOT NULL, nome VARCHAR(40), celular VARCHAR(15))'))
connection.commit()
~~~

## ORM

### Base Declarativa
~~~python
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

~~~

### Models
Vamos agora criar nosso modelos que são classes que herdam a classe `Base`
~~~python
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, String, Integer

class Contato(Base):
    __tablename__ = "contatos"
    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    nome = Column(String)
    celular = Column(String)

    def __repr__(self):
        return "Nome: " + self.nome + " | " + self.celular
~~~

### CRUD
~~~python

def insert_contato(session: Session, contato: Contato):
    db_contato = Contato(nome=contato.nome,celular=contato.celular)
    session.add(db_contato)
    session.commit()
    session.refresh(db_contato)
    return db_contato

def get_contatos(session: Session):
    return session.query(Contato).all()
~~~

Para inserir um contato instaciamos um objeto da classe `Contato` e chamamos o método `insert_contato`

~~~python
carlos = Contato (nome="Carlos Antônio", celular="87 9 1234")
insert_contato(session, carlos)
print(get_contatos(session))
~~~

