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