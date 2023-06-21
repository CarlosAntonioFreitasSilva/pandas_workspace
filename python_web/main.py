from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel


class Produto(BaseModel):
    nome: str
    preco: float



# uvicorn main:app --relaod
app = FastAPI()


@app.get("/")
def read_root():
    return {"mensagem": "Olá"}


# enviando parâmetro
@app.get("/nova_rota/{item}")
def read_item(item):
    return {"mensagem": item}


@app.get("/area/{largura}")
def calcular(largura: int):
    area = largura * largura
    return (f'A área do quadrado é {area}')


# parâmetro query não é definido na rota e são passados pela URL da forma <nome_da_rota?par1=valor&par2=valor>
# para definir valor padrão, caso não se enviado pela URL, basta atribuir fazendo da seguinte forma <cliente: str = "valor", total: float = "valor">
@app.get("/boleto")
def gerar_boleto(cliente: str, total: str):
    texto = f"Cliente: {cliente} ----- Total à pagar: R$ {total}"
    return (texto)


# requisições POST
@app.post("/produtos")
def produtos(produto: Produto):
    return {'mensagem': f'Produto {produto.nome} - R$ {produto.preco} cadastrado!'}
