quantidade = 10
print("Existem " + str(quantidade)+ " frutas no cesto")
print(f"Existem {quantidade} frutas no cesto")

# O uso da função format evita a utilização de casting
# exemplo 1
fruta = "laranja"

print('Suco de {} é o meu favorito!' .format(fruta))

# exemplo 2
cidade = "Petrolina"
uf = "PE"
dia = 14
mes = "março"
ano = 2023

print ('{} - {}, {} de {} de {}.' .format(cidade, uf, dia, mes, ano))