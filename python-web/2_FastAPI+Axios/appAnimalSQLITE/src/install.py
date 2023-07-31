import sqlite3
from sqlite3 import Error

diretorio = "C:\\SQLiteStudio\\database.db"
def conectar():
        try:
            con=sqlite3.connect(diretorio)
        except Error as ex:
            print(ex)
        return con

vcon = conectar()

sql_create = """CREATE TABLE IF NOT EXISTS animais(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(20),
        idade INT(2),
        sexo VARCHAR(10),
        cor VARCHAR(10)
)"""


def criarTabela(conexao,sql):
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        print("Tabela criada")
    except Error as ex:
        print(ex)

criarTabela(vcon,sql_create)

