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

sql_insert = "INSERT INTO contatos (`nome`,`celular`) VALUES ('Márcia Paes','99123456')"
sql_insert = "INSERT INTO animais (`nome`,`idade`,`sexo`,`cor`) VALUES ('Thor',9,'macho','Caramelo')"


def inserir(conexao,sql):
    try:
        cursor=conexao.cursor()
        cursor.execute(sql)
        conexao.commit()  #para fazer persistência no banco de dados
        print("Registro feito com sucesso!")
    except Error as ex:
        print(ex)

inserir(vcon,sql_insert)

