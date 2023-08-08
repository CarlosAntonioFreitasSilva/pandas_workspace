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
    id = Column(Integer, index=True,autoincrement=True)
    nome = Column(String)
    celular = Column(String, primary_key=True)

    def __repr__(self):
        return f"Contato(id={self.id}, nome = {self.nome}, celular = {self.celular})"
~~~

### CRUDS
Fazer o CREATE TABLE
#### Insert
~~~python

def insert_contato(session: Session, contato: Contato):
    new_contato = Contato(nome=contato.nome,celular=contato.celular)
    session.add(new_contato)
    session.commit()
    session.refresh(new_contato)
    return new_contato
~~~

#### Select


~~~python
def get_contatos(session: Session):
    return session.query(Contato).all()
~~~

Aplicando filtros
~~~python

def get_contato_celular(session: Session, celular: str):
    return session.query(Contato).filter(Contato.celular == celular).first()

def get_contato_nome(session: Session, nome: str):
    return session.query(Contato).filter(Contato.nome == nome).all()
~~~

## Executando o código
Para inserir um contato instaciamos um objeto da classe `Contato` e chamamos o método `insert_contato()`.

~~~python
carlos = Contato (nome="Carlos Antônio", celular="87 9 1234")
insert_contato(session, carlos)
~~~

Para fazer consulta pelo celular chamamos o método `get_contato_celular()` passando como argumento a sessão e o número de celular.

~~~python
print(get_contatos(session))
print(get_contato_celular(session, "87 9 0101"))
~~~

Consultando pelo nome
~~~python
print(get_contato_nome(session, "Marcia Paes"))
~~~
