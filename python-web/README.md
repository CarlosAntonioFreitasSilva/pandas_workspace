# Backend com Python

Para desenvolver a aplicação backend vamos utilizar o FastAPI que é um framework web para construção de aplicações Python baseado em padrões abertos
 - OpenAPI para criações de API, incluindo declarações de operações de rota, parâmetros, corpo de requisições
 - Modelo de dados com JSON Schema

Para instalar o FastAPI utilizamos no prompt de comando, do sistema operacional

`pip install fastapi[all]`


Comentários:
- Existem outros frameworks tais como Roadmap e Django para desenvolver aplicações python.
- No PHP existe o framework Lavarel que utiliza o padrão de operações de rota

## App OlaMundo
Crie o arquivo `main.py` para implementarmos o código.

### Importando FastAPI

~~~python
from fastapi import FastAPI
~~~

### Criando instância

Criamos uma instância da classe `FastAPI` e armazenamos numa variável no qual chamaremos de `app`

~~~python
from fastapi import FastAPI

app = FastAPI()
~~~

### Criando operações de rotas

Uma rota é a última parta da URL que começa a partir de `/`

As operações de métodos HTTP
- `GET`
- `POST`
- `PUT`
- `DELETE`

Vamos criar uma operação `GET` cuja rota é `/`

~~~python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message":"Olá, mundo"}
~~~

Ao acessar a rota `/` usando operação `GET` teremos como retorno o `dict`. 

Podemos retornar `list` e outros tipos de dados como `string`, `int`, páginas HTML e etc.


### Executando o código

Para executar o código acessamos o diretório do arquivo onde está a nossa aplicação, nesse caso, o arquivo `main.py` e digitamos o comando para iniciarmos o servidor

`uvicorn main:app --reload`

Observe que foi utilizado o nome do arquivo `main` e nome da variável que armazena a instância da classe `FastAPI` que é `app`.

Após o servidor ter sido inicializado acesse


- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/html`

## Parâmetros de rotas
Podemos criar parâmetros de rotas utilzando a mesma sintaxe usada pelo formato de strins do Python.

~~~
@app.get("/ola/{name}")
def root(name):
 return ("Olá" + name.capitlize())
~~~
Para acessar a rota passando argumentos utilizamos `http://127.0.0.1:8000/ola/carlos`

Podemos declarar o tipo de um parâmetro de rota usando a anotção usual do Python

~~~
@app.get("/ola/{name: str}")
def root(name):
 return ("Olá" + name.capitlize())
~~~

## Parâmetros Query

~~~python
@app.get("/ola")
def root(name):
    return "Olá " + name.capitalize()
~~~

O método `capitalize()` foi utilizado para a primeira letra do nome ficar maiúscula.

Para passar parâmetros pelo URL utilizamos `URL/ola/?nome=arg`. No nosso caso acessamos
`http://127.0.0.1:8000/ola/?nome=carlos`

## Método post

~~~python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    firstname: str
    lastname: str

@app.post('/')
def root(user: User):
    return user
~~~
Resposta da requisição é um JSON

~~~json
{
  "firstname": "string",
  "lastname": "string"
}
~~~
# Cliente/Servidor

Fazer uma introdução....
~~~python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    firstname: str
    lastname: str

@app.post('/')
def root(user: User):
    return user
~~~

<p style="text-align:center"><img src="https://miro.medium.com/v2/resize:fit:720/format:webp/1*4SEvcz6KvyaqOqBpJABTBg.png" style="width:400px" /></p>


## Axios

Para enviar requisições HTTP do lado do cliente podemos utilizar o Axios que é um cliente HTTP baseado em promessas e utiliza `XMLHttpRequest` do Javascript no lado do cliente e roda no lado do servidor utilizando `node.js` 
<br><br>

.....
