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

Podemos retornar `list` e outros tipos de dados como `string`, `int`, modelos `Pydantic` e etc.

Para retornar HTML devemos importar `HTMLResponse` e adicionamos o parâmetro `response_class=HTMLResponse` na operação `GET`. Para exemplificar, vamos criar um rota `/html` que retorna uma página HTML. 

~~~python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get('/')
def root():
    return {"message": "Olá, mundo"}

@app.get('/html', response_class=HTMLResponse)
def root():
    return """
    <html lang="pt-br">
        <head>
            <title>APP Hello</title>
        </head>
        <body>
            <h1>Olá, mundo!</h1>
            <p>Esta é minha primeira página HTML</p>
        </body>
    </html>
~~~

### Executando o código

Para executar o código acessamos o diretório do arquivo onde está a nossa aplicação, nesse caso, o arquivo `main.py` e digitamos o comando para iniciarmos o servidor

`uvicorn main: app --reload`

Observe que foi utilizado o nome do arquivo `main` e nome da variável que armazena a instância da classe `FastAPI` que é `app`.

Após o servidor ter sido inicializado acesse


- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/html`

## Parâmetros de rotas

~~~python
@app.get("/ola")
def root(nome):
    return "Olá " + nome.capitalize()
~~~

O método `capitalize()` foi utilizado para a primeira letra do nome ficar maiúscula.

Para passar parâmetros pelo URL utilizamos `URL/ola/?nome=arg`. No nosso caso acessamos
`http://127.0.0.1:8000/ola/?nome=carlos`


Parei de estudar em https://fastapi.tiangolo.com/tutorial/query-params/

# Cliente/Servidor

Para enviar requisições HTTP do lado do cliente podemos utilizar o Axios que é um cliente HTTP baseado em promessas e utiliza `XMLHttpRequest` do Javascript no lado do cliente e roda no lado do servidor utilizando `node.js`

Vamos criar uma página HTML com formulário que envia nome e número de telefone para o servidor pelo Javascript.

## Lado do cliente

Vamos criar a página `index.html`

~~~html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <script src="index.js"></script>
</head>

<body>
    <form id="form">
        <input type="text" id="nome" placeholder="Nome">
        <input type="text" id="celular" placeholder="Celular">
        <input type="submit" value="OK" id="submit">
    </form>
</body>

</html>
~~~

Adicionamos a tag `script` para usar o Axios via CDN do jsDelivr e o nosso código javascript que será implementado no arquivo `index.js`.

### Index.js
No arquivo `index.js` vamos implementar o código que adiciona o evento `submit` no formulário e ao ser acionado criamos uma função anônima para manipular o evento. 

**Observação:** No nosso exemplo a aplicação que irá receber os dados do formulário estará em `http://127.0.0.1:8000/gravar/` que iremos implementar logo adiante. Criaremos um arquivo python com a rota `/gravar` que utiliza a operação `POST`.


~~~javascript
window.onload = function () {
    document.getElementById("form").onsubmit = function (event) {
        
        event.preventDefault()  //para não dar refresh na página quando acontecer o submit
        const nome = document.getElementById('nome')
        const celular = document.getElementById('celular')

        axios.post('http://127.0.0.1:8000/gravar/', {
            nome: nome.value,
            celular: celular.value
        })
            .then(function (response) {
                // manipula o sucesso da requisição
                console.log(response);
            })
            .catch(function (error) {
                // manipula erros da requisição
                console.error(error);
            })
            .finally(function () {
                // sempre será executado
            });
    }

}
~~~

## Lado do servidor
A aplicação que roda no lado servidor que será chamada main.py

Vamos criar a rota `\gravar` que recebe os dados `nome` e `celular` enviados pelo formulário pela operação `POST`.

~~~python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ['http://127.0.0.1:5500']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.post('/gravar/')
def root(): 
    return {"message":"ok"}
~~~

A requisição enviada do cliente tem sua origem no host `http://127.0.0.1:5500` e a aplicação do lado servidor está em `http://127.0.0.1:8000` e assim temos uma requisição de uma origem externa. Nesse caso utilizamos `CORSMiddleware` para permitir que a aplicação possa receber requisições de outras origens, caso contrário, a política de segurança do CORS não ira permitir.

Até aqui a nossa rota não está recebendo os dados do formulário e quando o formulário é submetido apenas recebemos um `JSON` com mensagem de ok. 

Para receber os dados do formulário precisamos criar um modelo de dados com `pydantic` de `BaseModel`.

~~~python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = ['http://127.0.0.1:5500']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class Contato(BaseModel):
    nome: str
    celular: str

@app.post('/gravar/')
def root(contato: Contato): 
    return contato.nome + contato.celular
~~~

Para que nossa aplicação fique mais completa podemos implementar um código que os dados do formulário sejam armazenados em um banco de dados.
