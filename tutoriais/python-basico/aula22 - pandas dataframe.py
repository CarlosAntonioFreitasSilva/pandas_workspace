# Import pandas
import pandas as pd

# dictionary
data = {
  "Duration": [60,60,60,45,45,60,60,45],
  "Pulse":[110,117,103,109,117,102,110,104],
  "Maxpulse": [130,145,135,175,148,127,136,134],
  "Calories": [409.1,479.0,340.0,282.4,406.0,300.0,374.0,253.3]
}

#create a DataFrame object:
data_dictionary = pd.DataFrame(data)

# Display DataFrame data_dictionary
print(data_dictionary.info()) # dataframe structure
print(data_dictionary.head()) # dataframe fist 5 rows

# load the 'data.csv' into a DataFrame
data_dataset = pd.read_csv("G:/Meu Drive/python_basico/perimetro_cefalico.csv")

# Display DataFrame data_dataset
print(data_dataset.info()) # dataframe structure
print(data_dataset.head()) # dataframe fist 5 rows
