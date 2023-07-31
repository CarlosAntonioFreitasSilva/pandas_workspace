from fastapi import FastAPI, Path
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from pydantic import BaseModel
import sqlite3
from sqlite3 import Error

app = FastAPI()

# Permitir requisições de origens diferentes do backend
origins = ['http://127.0.0.1:5500']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


class Animal(BaseModel):
    id: Optional[str]
    nome: str
    idade: int
    sexo: str
    cor: str

diretorio = "C:\\SQLiteStudio\\database.db"


def conectar():
        try:
            con=sqlite3.connect(diretorio)
        except Error as ex:
            print(ex)
        return con


def inserir(conexao,sql):
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        conexao.commit()  #para fazer persistência no banco de dados
        print("Registro feito com sucesso!")
    except Error as ex:
        print(ex)


def consultar(conexao,sql):
    cursor = conexao.cursor()
    cursor.execute(sql)
    return cursor.fetchall()


@app.get('/animais')
def listar_animais():
    sql_select = "SELECT * FROM animais"
    vcon = conectar()
    registros = consultar(vcon,sql_select)
    return registros


@app.get('/animais/{animal_id}')
def obter_animal(animal_id: str):
    for animal in banco:
        if animal.id == animal_id:
            return animal
    return {'erro': 'Animal não localizado'}


@app.delete('/animais/{animal_id}')
def remover_animal(animal_id: str = Path(..., title='Código do animal a se buscar')):
    posicao = -1
    # buscar o posicao do animal
    for index, animal in enumerate(banco):
        if animal.id == animal_id:
            posicao = index
            break

    if posicao != -1:
        banco.pop(posicao)
        return {'mensagem': 'Animal removido com sucesso'}
    else:
        return {'erro': 'Animal não localizado'}


@app.post('/animais')
def criar_animal(animal: Animal):
    sql_insert = f"INSERT INTO animais (`nome`,`idade`,`sexo`,`cor`) VALUES ('{animal.nome}','{animal.idade}','{animal.sexo}','{animal.cor}')"
    vcon = conectar()
    inserir(vcon,sql_insert)
    return None