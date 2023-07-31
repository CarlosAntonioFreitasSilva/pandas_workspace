from fastapi import FastAPI, Path
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from pydantic import BaseModel
import sqlite3
from sqlite3 import Error

# uvicorn main:app --reload
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


class Pessoa(BaseModel):
    id: Optional[str]
    nome: str
    cpf: int


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


@app.get('/pessoas')
def listar_pessoas():
    sql_select = "SELECT * FROM pessoa"
    vcon = conectar()
    registros = consultar(vcon,sql_select)
    return registros


@app.post('/pessoas')
def criar_pessoas(pessoa: Pessoa):
    sql_insert = f"INSERT INTO pessoa (`nome`,`cpf`) VALUES ('{pessoa.nome}','{pessoa.cpf}')"
    vcon = conectar()
    inserir(vcon,sql_insert)
    return None