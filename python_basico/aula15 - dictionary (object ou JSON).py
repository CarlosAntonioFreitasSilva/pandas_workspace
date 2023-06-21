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