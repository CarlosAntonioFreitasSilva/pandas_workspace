coluna1=[2,2]
coluna2=[2,2]
matriz = [coluna1,coluna2]

determinante = matriz[0][0]*matriz[1][1]-matriz[0][1]*matriz[1][0]

print(determinante)
if determinante == 0:
    print("A matriz é singular")
else:
    print("A matriz é não singular")