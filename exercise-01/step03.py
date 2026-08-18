from __init__ import jm1_data

data = jm1_data

"""
Etapa 3 – Análise dos defeitos 
Separe os registros em dois grupos: 
módulos com defeito; 
módulos sem defeito. 
Para a variável escolhida, calcule a média e o desvio-padrão de cada grupo. 
"""

with_defect = data[data["defects"] == True]
without_defect = data[data["defects"] == False]

print("Mean of with defect", round(with_defect["loc"].mean(), 2))
print("Mean of without defect", round(without_defect["loc"].mean(), 2))

print("Standard deviation of with defect", round(with_defect["loc"].std(), 2))
print("Standard deviation of without defect", round(without_defect["loc"].std(), 2))
