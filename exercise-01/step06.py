from __init__ import reduced_software_project_risk_data

data = reduced_software_project_risk_data

"""
Escolha duas variáveis quantitativas. 

Para cada variável, calcule: 
média; 
mediana; 
moda, quando aplicável; 
mínimo; 
máximo; 
amplitude; 
variância; 
desvio-padrão.

Actual_Effort_Hours, Estimated_Effort_Hours
"""

print(data["Actual_Effort_Hours"].mean())
print(data["Estimated_Effort_Hours"].mean())

print()

print(data["Actual_Effort_Hours"].median())
print(data["Estimated_Effort_Hours"].median())

print()

print(data["Actual_Effort_Hours"].mode())
print(data["Estimated_Effort_Hours"].mode())

print()

print(data["Actual_Effort_Hours"].min())
print(data["Estimated_Effort_Hours"].min())

print()

print(data["Actual_Effort_Hours"].max())
print(data["Estimated_Effort_Hours"].max())

print()

print(data["Actual_Effort_Hours"].max() - data["Actual_Effort_Hours"].min())
print(data["Estimated_Effort_Hours"].max() - data["Estimated_Effort_Hours"].min())

print()

print(data["Actual_Effort_Hours"].max() - data["Actual_Effort_Hours"].var())
print(data["Estimated_Effort_Hours"].max() - data["Estimated_Effort_Hours"].var())

print()

print(data["Actual_Effort_Hours"].max() - data["Actual_Effort_Hours"].std())
print(data["Estimated_Effort_Hours"].max() - data["Estimated_Effort_Hours"].std())
