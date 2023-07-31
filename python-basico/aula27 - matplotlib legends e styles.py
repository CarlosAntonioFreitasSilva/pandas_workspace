import pandas as pd
from matplotlib import pyplot as plt

atacado_dictionary={"mes":["Janeiro","Fevereiro", "Março","Abril","Maio","Junho"], "valor":[2.0,1.7,2.0,1.9,2.2,2.2]}
varejo_dictionary={"mes":["Janeiro","Fevereiro", "Março","Abril","Maio","Junho"],  "valor":[2.2,1.9,1.8,2.0,2.3,1.7]}
atacado = pd.DataFrame(atacado_dictionary)
varejo = pd.DataFrame(varejo_dictionary)
plt.style.use('seaborn')
plt.plot(atacado.mes,atacado.valor,label="Vendas no atacado", color="#FACC2E", linewidth=2, linestyle="--", marker="o")  
plt.plot(varejo.mes,varejo.valor,label="Vendas no varejo", color="#2E64FE", linewidth=2, linestyle=":", marker="d")
plt.xlabel("Mês")
plt.ylabel("R$ em milhões")
plt.legend()
plt.show()
