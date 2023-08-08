
try:
    print(2/0)
except NameError:
    print("Houve algum erro" + NameError)
finally:
    print("O programa foi finalizado")