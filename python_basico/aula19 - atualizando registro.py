import sqlite3
from sqlite3 import Error

diretorio="C:\\SQLiteStudio\\database.db"
def conectar():
        try:
            con=sqlite3.connect(diretorio)
        except Error as ex:
            print(ex)
        return con

vcon = conectar()

sql_create = """CREATE TABLE IF NOT EXISTS contatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(20),
        celular INT(10)
)"""

def criarTabela(conexao,sql):
    try:
        cursor=conexao.cursor()
        cursor.execute(sql)
    except Error as ex:
        print(ex)

criarTabela(vcon,sql_create)

sql_update = "UPDATE contatos SET nome='Guilherme' , celular = 2134 WHERE  id=3"

def atualizar(conexao,sql):
    try:
        cursor=conexao.cursor()
        cursor.execute(sql)
        conexao.commit()  #para fazer persistência no banco de dados
        print("Atualização feita com sucesso!")
    except Error as ex:
        print(ex)

atualizar(vcon,sql_update)

