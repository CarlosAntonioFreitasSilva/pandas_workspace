from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3
from sqlite3 import Error

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

data_base = "C:\\SQLiteStudio\\database.db"
def conectar():
        try:
            con=sqlite3.connect(data_base)
        except Error as ex:
            print(ex)
        return con

def insert(connection,sql):
    try:
         connection.cursor().execute(sql)
         connection.commit()
    except Error as ex:
        return ex
    
def select(connection,sql):
    return connection.cursor().execute(sql).fetchall()

@app.post('/gravar/')
def register(contato: Contato): 
    try:
        sql_insert = f"INSERT INTO contatos (`nome`,`celular`) VALUES ('{contato.nome}','{contato.celular}')"
        vcon = conectar()
        insert(vcon,sql_insert)
    except Error as ex:
        return ex
    
@app.get('/')
def ini():
    sql_select = f"SELECT * FROM contatos"
    vcon = conectar()
    return select(vcon,sql_select)