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

sql_select = "SELECT * FROM contatos"

def consultar(conexao,sql):
    cursor = conexao.cursor()
    cursor.execute(sql)
    return cursor.fetchall()

registros = consultar(vcon,sql_select)
for x in registros:
     print(x)

