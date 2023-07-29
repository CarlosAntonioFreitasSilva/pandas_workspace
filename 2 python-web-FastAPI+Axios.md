# Cliente/Servidor

<p style="text-align:center"><img src="https://miro.medium.com/v2/resize:fit:720/format:webp/1*4SEvcz6KvyaqOqBpJABTBg.png"/></p>

Para enviar requisições HTTP do lado do cliente podemos utilizar o Axios que é um cliente HTTP baseado em promessas e utiliza `XMLHttpRequest` do Javascript no lado do cliente e roda no lado do servidor utilizando `node.js` 
<br><br>

# appContacts

Vamos criar um projeto que contém uma página HTML com formulário que envia o nome e número de telefone para uma aplicação Python que fica do lado do servidor. Para implementar o envio dos dados do formulário utilizaremos a linguagem Javascript.

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
    document.getElementById("form").onsubmit = function () {

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

A requisição enviada do cliente tem sua origem no host `http://127.0.0.1:5500` e a aplicação do lado servidor está em `http://127.0.0.1:8000` e, sendo assim, temos uma requisição de uma origem externa. Nesse caso, utilizamos `CORSMiddleware` para permitir que a aplicação possa receber requisições de outras origens, caso contrário, a política de segurança do CORS não irá permitir.

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

Faremos isso adiante!

continuar ...
