def saudar(nome):
    print('Olá, ' + nome)

saudar("Carlos")

def validar():
    email = ""
    while '@' not in email:
        email = input('Digite seu e-mail ')
    print('E-mail cadastrado com')
validar()