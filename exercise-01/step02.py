from __init__ import data

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
print(f"Média:", round(data["loc"].mean(), 2))
print(f"Mediana:", round(data["loc"].median(), 2))
print(f"Mínumo:", round(data["loc"].min(), 2))
print(f"Máximo:", round(data["loc"].max(), 2))
print(f"Amplitude:", round(data["loc"].max() - data["loc"].min(), 2))
print(f"Variância:", round(data["loc"].var(), 2))
print(f"Desvio-padrão:", round(data["loc"].std(), 2))