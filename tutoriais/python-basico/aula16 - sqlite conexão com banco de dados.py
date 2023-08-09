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