# SQL Alchemy - Tutorial
## Engine
Já com o banco de dados criado, chamado `database`,  no diretório do projeto vamos criar o engine.
~~~python
from sqlalchemy import create_engine
engine = create_engine("sqlite:///./database.db", echo=True)
~~~

## Executando ORM  com Sessões
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

### Entities
Vamos agora criar nosso modelos que são classes que herdam a classe `Base`
~~~python
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Contato(Base):
    __tablename__ = "contatos"
    nome : Mapped[str] = mapped_column(String(30))
    celular: Mapped[str] = mapped_column(String(30), primary_key=True)

    def __repr__(self):
        return f"Contato(nome = {self.nome}, celular = {self.celular})"
~~~
### DDL

~~~python
Base.metadata.create_all(engine)
~~~


### Manipulação de dados com ORM


#### Insert
Para inserir um registro na tabela de contatos criamos primeiro uma instância de classe `Contato` e usamos o método `add()` como mostra o código a seguir:
~~~python

jose = Contato(nome="José Paulo",celular = "62 9 8976")
carlos = Contato(nome="Carlos Freitas",celular = "78 9 8976")
session.add(carlos)
session.add(jose)
session.commit()
~~~

#### Select

Para obter todos os registros de uma tabela devemos importar o método `select()` e vamos criar nossa declaração na variável `stmt` e logo utilizamos o método `execute()` passando como argumento a variável `stmt`.

~~~python
from sqlalchemy import select
stmt = select(Contato)
session.execute(stmt).all()
~~~

**Selecionando pela chave primária**
Para selecionar um registro pela chave primária utilizamos `session.get(Entidade, valor_da_chave)`

~~~python
session.get(Contato,"Antônio")
~~~

**Selecionando colunas**
~~~python
stmt = select(Contato.nome)
session.execute(stmt).all()
~~~

**Aplicando filtros**

~~~python
stmt = select(Contato).where(Contato.nome == "Carlos Freitas")
session.execute(stmt).first()
session.execute(stmt).all()
~~~

**Ordenando registos**

~~~python
stmt = select(Contato).order_by(Contato.nome)
session.execute(stmt).all()

order_desc = select(Contato).order_by(Contato.nome.desc())
session.execute(order_desc).all()
~~~


#### Update

~~~python
from sqlalchemy import update

stmt = update(Contato).where(Contato.nome == "Carlos Freitas").values(nome = "Carlos Antônio)
session.execute(stmt)
session.commit()
~~~

#### Delete
~~~python
from sqlalchemy import delete

stmt = delete(Contato).where(Contato.celular == "78 9 8976")
session.commit()

~~~
