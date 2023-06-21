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