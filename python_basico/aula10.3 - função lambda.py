def soma(a,b):
    return a+b

print(soma(4,3))

soma = lambda a, b: a+b
print(soma(5,7))


# a função lambda pode ser sobrescrita, sendo assim é preciso cuidado na hora de usar
x = lambda: "Uma função"
x = "Uma string"
print(x)
 