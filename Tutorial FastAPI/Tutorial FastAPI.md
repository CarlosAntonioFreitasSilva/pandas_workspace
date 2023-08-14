# Requisições HTTP

O HTTP é um protocolo da camada de aplicação do modelo TCP/IP que é utilizado em serviços de transferência de arquivos HTML. O cliente solicita ao servidor uma página HTML (verificar melhor esse texto. Afinal o cliente solicita só paginas HTML?) e o servidor envia a pagina em resposta ao ciente. O endereço da página solicitada é a URL, que é enviada na solicitação. 

<img src="https://materiais.imd.ufrn.br/materialV2/assets/imagens/sistemas-de-conectividade/sistemas_conectividade_a06_2016_Aula_06_Modelos_Comunicacao_Redes_Figura_02.jpg"/>

Ao solicitar ao servido algum arquivo HTML temos uma requisição (request) e o servidor envia uma resposta(response) ao cliente.

Descrever como é o corpo de uma requisição HTTP...header, método GET POST e etc...


~~~python
from fastapi import FastAPI
app =FastAPI()

@app.get("/")
def root():
    return "Olá, GET"

@app.post("/")
def root():
    return f"Olá, POST!"
~~~



~~~python
@app.get("/home")
def root(firstname: str, lastname: str):
    return f"Olá,  {firstname}  {lastname} !"

@app.post("/home")
def root(firstname: str, lastname: str):
    return f"Olá,  {firstname}  {lastname}!"
~~~


# Pydantic

~~~python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post("/items/")
async def create_item(item: Item):
    return f"{item.name} {item.description}"

~~~

# Templates
Instalar jinja2   

`pip install jinja2`

~~~python
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory = "templates")

@app.get("/index1")
async def root(request: Request):
    return templates.TemplateResponse("index1.html",{"request":request})
~~~



# Retornando dados para o Frontend
~~~python
frutas = ["banana", "maçã", "laranja", "maracujá"]
cliente = {"nome":"Carlos", "celular":"9 8 3986"}
class Pessoa:
    def __init__(self,nome,cpf,data_nasc):
        self.nome = nome
        self.cpf = cpf
        self.data_nasc = data_nasc

jose = Pessoa("José",788787,"1988")
item = Item(name = "Notebook", description = "Lenovo, CORE I3", price = 243.54,tax = None)

@app.get("/index3")
async def root(request: Request):
    return templates.TemplateResponse("index3.html",{"request":request, "dados_list": frutas, "dados_dict": cliente, "pessoa":jose, "item": item })

~~~

# Fomulários
~~~python
from fastapi import Form

@app.get("/form", response_class = HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("form.html",{"request":request})

@app.post("/form")
def root(firstname: str = Form(), lastname: str = Form()):
    return f"Olá,  {firstname}  {lastname}!"
~~~


# Requisições com XMLHttpRequest

~~~python
@app.get("/index2")
async def root(request: Request):
    return templates.TemplateResponse("index2.html",{"request":request})

@app.post("/XMLHttpRequest1")
def root(firstname: str, lastname: str):
    return {"firstname":firstname,"lastname":lastname}


class Pessoa(BaseModel):
    firstname: str
    lastname: str
    
@app.post("/XMLHttpRequest2")
def root(pessoa: Pessoa):
    return pessoa
~~~