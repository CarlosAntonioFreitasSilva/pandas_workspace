import pandas as pd
from matplotlib import pyplot as plt


# Load the 'ransom.csv' into a DataFrame
data_frame = pd.read_csv("C:/pythonBasico/data.csv")
plt.splot(data_frame.Duration,data_frame.Calories)
plt.xlabel("Duration")
plt.ylabel("Calories")      
plt.title("Título do gráfico")
plt.show()

