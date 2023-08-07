import pandas as pd
from matplotlib import pyplot as plt



year = [1950,1970,1990,2010]
pop = [2.519, 3.692, 5.263, 6.972]
plt.plot(year, pop)
plt.show()



# usando dataframe
data_frame = pd.read_csv("C:/python_basico/data.csv")
plt.plot(data_frame.Duration,data_frame.Calories)
plt.show()

notas_dictionary={"nome":["Ana","João","Carlos"], "nota":[9,8,8.5]}
notas = pd.DataFrame(notas_dictionary)
plt.plot(notas.nome,notas.nota)
plt.show()
