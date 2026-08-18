from __init__ import jm1_data

data = jm1_data
"""
Etapa 2 – Seleção de uma variável quantitativa 
Escolha uma variável quantitativa relacionada às características do software.

média; 
mediana; 
mínimo; 
máximo; 
amplitude; 
variância; 
desvio-padrão. 
"""
print("Média:", round(data["loc"].mean(), 2))
print("Mediana:", round(data["loc"].median(), 2))
print("Mínumo:", round(data["loc"].min(), 2))
print("Máximo:", round(data["loc"].max(), 2))
print("Amplitude:", round(data["loc"].max() - data["loc"].min(), 2))
print("Variância:", round(data["loc"].var(), 2))
print("Desvio-padrão:", round(data["loc"].std(), 2))
