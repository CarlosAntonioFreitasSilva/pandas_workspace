import math
import datetime
import sqlite3 # banco de dados
import pandas as pd #analise de dados
fatorial = math.factorial(9)
print(fatorial)


data = datetime.date.today()
dia = datetime.date.today().day
mes = datetime.date.today().month
ano = datetime.date.today().year
print('A data de hoje é {}' .format(data))
print ('Petrolina, {}/{}/{}' .format(dia,mes,ano))

