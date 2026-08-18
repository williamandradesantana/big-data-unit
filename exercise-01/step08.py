from __init__ import reduced_software_project_risk_data

import matplotlib.pyplot as plt
import pandas as pd

data = reduced_software_project_risk_data

"""
Etapa 4 - Gráficos

1 histograma;
1 boxplot;
1 gráfico de barras relacionando uma variável categórica ao nível de risco.
"""

data["Risk_Level"] = pd.cut(
    data["Risk_Score"], bins=3, labels=["Low", "Medium", "High"]
)

plt.hist(data["Actual_Effort_Hours"], bins=10)

plt.title("Distribuição do esforço realizado")
plt.xlabel("Esforço realizado (horas)")
plt.ylabel("Frequência")

plt.show()

low = data[data["Risk_Level"] == "Low"]["Actual_Effort_Hours"]
medium = data[data["Risk_Level"] == "Medium"]["Actual_Effort_Hours"]
high = data[data["Risk_Level"] == "High"]["Actual_Effort_Hours"]

plt.boxplot([low, medium, high])

plt.title("Esforço realizado por nível de risco")
plt.xlabel("Nível de risco")
plt.ylabel("Esforço realizado (horas)")
plt.xticks([1, 2, 3], ["Baixo", "Médio", "Alto"])

plt.show()

risk_complexity = pd.crosstab(data["Complexity_Level"], data["Risk_Level"])

risk_complexity.plot(kind="bar")

plt.title("Nível de risco por complexidade do projeto")
plt.xlabel("Nível de complexidade")
plt.ylabel("Quantidade de projetos")

plt.show()
