# Import pandas
import pandas as pd

# Load the 'data.csv' into a DataFrame
data_dataset = pd.read_csv("G:/Meu Drive/python_basico/data.csv")

# Display DataFrame
print(data_dataset.info())  

pulse = data_dataset[data_dataset["Pulse"] == 110]
duration = data_dataset[data_dataset.Duration == 60]
pulse_bool = data_dataset["Pulse"] == 100
print(pulse)
print(duration)
print(pulse_bool)

