# Variáveis

Diferente do Java, na linguagem Python não precisamos declarar o tipo de variável ao ser declarada. O tipo da variável é definido ao ser atribuído um valor.

~~~python
x = 5  #int
y = 23.678  #float
z = True  #bool
w = False # bool
nome = "Carlos"  #string
~~~
O método type retorna o tipo da variável.

~~~python
print(type(x))
print(type(y))
print(type(z))
print(type(w))
print(type(nome))
~~~

# f-string

~~~pyhon
faturamento = 1000
print(f"Faturamento: R$ {faturamento} ")

quantidade = 10
print("Existem " + str(quantidade)+ " frutas no cesto")
print(f"Existem {quantidade} frutas no cesto")
~~~


# Função format

O uso da função format evita a utilização de casting
## exemplo 1
~~~python
fruta = "laranja"

print('Suco de {} é o meu favorito!' .format(fruta))
~~~
## exemplo 2
~~~python
cidade = "Petrolina"
uf = "PE"
dia = 14
mes = "março"
ano = 2023

print ('{} - {}, {} de {} de {}.' .format(cidade, uf, dia, mes, ano))
~~~

# Função input
~~~python
nome = input("Qual é o seu nome?")

print("Olá, " + nome + "!")
~~~

# Operadores aritméticos

~~~pyhton

print(8+3) #soma 
print(4-6) #subtração
print(4*8)  #multiplicação
print(2**10) #potencia
print(7/3)  #divisão
print (7//3)  # parte inteira da divisão
print(7%3)  #resto da divisão
~~~

# List

~~~python
carros = ["HRV", "Corola","Polo","Fusca"]
print(type(carros))
print(carros[1])
print(carros.index("Corola"))
carros[1]="Palio"
print(carros)
carros.append("S-10")
carros.append("HB-20")
print(carros)
print(len(carros))
carros.remove("Polo")
print(carros)


lista = ["banana", 23, 2.5489, "cidade", False,"cidade","cidade"]
for x in lista:
    print(x)

print(f' A palavra cidade aparece {lista.count("cidade")} vezes')   
# Método de listas
# my_list = []

# my_list.index.(arg)
# my_list.count(arg)
# my_list.upper()
# my_list.reverse()
# sorted(my_list, reverse=False[optional] )
~~~

# Tuplas

~~~python
carros = ("Polo", "Corolla","Fusion")
print(type(carros))
for x in carros:
    print(x)
~~~

# Dictionary

~~~python
pessoa ={
    "nome":"Carlos Antônio",
    "cpf": "013.654.321-00",
    "celular":"(99) 9 9999-9999",
    "email":"email@email.com"
}

print(type(pessoa))
print(pessoa["nome"]+ ", inscrito no CPF " + pessoa["cpf"])
#pode utilizar o método get
print("O contato de " + pessoa.get("nome") + " é " + pessoa.get("celular"))

for x in pessoa:
    print(x)  #imprime chave

for x in pessoa:
    print(pessoa[x]) #imprime valor

# Create the years and durations lists
years = [2011,2012,2013,2014,2015,2016,2016,2017,2018,2019,2020]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93,90]

# Create a dictionary with the two lists
movie_dict = {"years":years, "durations":durations}
print(movie_dict)
~~~


# Decisões

~~~python
x = False

if(x==True):
    print("Sistema está ligado")
else:
    print("Sistema está desligado")

a = 2
b = 5

if(a>b):
    print("a é maior que b")
else:
    print("a é menor que b")


nome = "papai"

if(nome == "mamãe"):
    print('Eba!')
else:
    print('Não é mamãe!')


ano = int(input("Informe o ano do seu nascimento "))
idade = 2023 - ano
if(idade>=18):
    print("Você é adulto")
else:
    print("Você ainda é menor")
~~~

# Loop for
~~~python
# loop for para intervalo
for i in range(5):
    print(i)
 #observe que a variável i começa em zero


# loop for para strings
palavra = "Python"
for i in palavra:
    print(i)

# loop for para lists
lista = ["arroz", "feijão", "café", "açucar"]

for i in lista:
    print(i)

house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
for i in house:
    print ("the " + str(i[0]) + " is " + str(i[1]) + " sqm")


# loop for para dictionaries
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
for key, value in europe.items():
    print(f"the capital of {key} is {value}")

# loop for para np.arrays

# loop for para dataframes
import pandas as pd
datas = pd.read_csv('data.csv', index_col = 0)

# Iterate over datas
for val in datas:
    print(val)

# Iterate over rows of datas iterrows()
for lab, row in datas.iterrows():
    print(lab)
    print(row)
~~~