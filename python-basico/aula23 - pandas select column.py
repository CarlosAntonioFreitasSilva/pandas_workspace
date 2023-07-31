# Import pandas
import pandas as pd

# Load the 'data.csv' into a DataFrame
data_dataset = pd.read_csv("G:/Meu Drive/python_basico/data.csv")

# Display DataFrame
print(data_dataset.info())  

#Selecionando uma coluna
print(data_dataset.Calories.head()) 
print(data_dataset["Calories"].head()) 

# selecionando varias colunas 
print(data_dataset[["Duration","Calories"]].head())