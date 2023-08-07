def soma(a,b):
    return a+b

print(soma(4,3))

soma = lambda a, b: a+b
print(soma(5,7))

soma = lambda a,b,c:a+b+c

print(soma(2,3,5))


# a função lambda pode ser sobrescrita, sendo assim é preciso cuidado na hora de usar
x = lambda: "Uma função"
x = "Uma string"
print(x)
 