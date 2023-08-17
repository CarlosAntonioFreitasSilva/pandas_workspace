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

session.execute(text('CREATE TABLE contatos (nome VARCHAR (40) NOT NULL, celular VARCHAR (15) NOT NULL PRIMARY KEY)'))
session.commit()
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
    nome = Column(String)
    celular = Column(String, primary_key=True)

    def __repr__(self):
        return f"Contato(nome = {self.nome}, celular = {self.celular})"
~~~

### CRUDS


#### Insert
Para inserir um registro na tabela utilizamos uma instância de classe `Contato` como mostra o código a seguir:
~~~python

jose = Contato(nome="José Paulo",celular = "62 9 8976")
session.add(jose)
session.commit()
session.refresh(jose)

~~~

#### Select

Para obter todos os registros de uma tabela passamos como argumento para o método `query()` o nome da classe que está fazendo o mapeamento.

~~~python
session.query(Contato).all()
~~~

**Aplicando filtros**

~~~python

session.query(Contato).filter(Contato.nome == "Carlos Antônio").first()

session.query(Contato).filter(Contato.nome == "Carlos Antônio").all()
~~~

#### Update
~~~python
session.query(Contato).filter(Contato.celular == "87 9 1234").update({"nome":"Carlos Freitas"})
session.commit()
~~~

#### Delete
~~~python
session.query(Contato).filter(Contato.nome == "Carlos Antônio").delete()
session.commit
~~~
