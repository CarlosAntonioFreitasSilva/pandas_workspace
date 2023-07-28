# Banco de dados SQLite

Para conexão com banco de dados utiliza-se `sqlite3.connect(dir) ` passando como parametro o diretório do banco de dados a ser conectado. Vamos criar o método `conectar()` que ao ser chamado irá executar tal comando.
~~~py
import sqlite3
from sqlite3 import Error

diretorio=""C:\\SQLiteStudio\\database.db""
def conectar():
        try:
            con=sqlite3.connect(diretorio)
        except Error as ex:
            print(ex)
        return con

~~~
Vamos criar a variável `vcon` para armazenar a conexão com o banco de dados
~~~
vcon = conectar()
~~~
### Criando tabela
Para criar tabela utilizamos o comando  `CREATE TABLE` da linguagem SQL e armazenamos na variável `vsql`
~~~py
vsql = """CREATE TABLE contatos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(20),
        celular INT(10)
)"""
~~~
Criamos uma função `criarTabela(conexao,sql)` que deve receber como parâmetro a conexão e o comando sql a ser executado que está armazenado na variável `vsql`.
~~~
def criarTabela(conexao,sql):
    try:
        cursor=conexao.cursor()
        cursor.execute(sql)
    except Error as ex:
        print(ex)
~~~
A classe Cursor permite que o código Python execute comandos SQL em uma sessão de banco de dados. Os cursores estão vinculados à conexão e utilizamos o método `cursor()`.

Para executar o comando bastar fazermos a chamada da função passando como parâmetro as varáveis `vcon` e `vsql`.
~~~py
criarTabela(vcon,vsql)
~~~
### Inserindo registro 

Para inserir registro utilizamos o comando `INSERT INTO`, da lingugem SQL, que será armazenada na variável `vsql`
~~~py
vsql = "INSERT INTO contatos (`nome`,`celular`) VALUES ('Carlos','99123456')"
~~~
Construímos a função `inserir(conexao,sql)` que recebe como parametro a conexao e o comando SQL a ser executado da variável `vsql`.
~~~py
def inserir(conexao,sql):
    try:
        cursor=conexao.cursor()
        cursor.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
~~~
O método `commit()` faz a persistência do registro.
~~~py
inserir(vcon,vsql)
~~~

### Consulta

A consulta `SELECT` executada pelo cursor utilizamos o método `fetchall()` que retorna os registros da consulta.

~~~py
vsql = "SELECT * FROM contatos"

def consultar(conexao,sql):
    cursor=conexao.cursor()
    cursor.execute(sql)
    return cursor.fetchall()
~~~
