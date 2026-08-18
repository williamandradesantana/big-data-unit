from __init__ import jm1_data

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
print(f"Média:", round(jm1_data["loc"].mean(), 2))
print(f"Mediana:", round(jm1_data["loc"].median(), 2))
print(f"Mínumo:", round(jm1_data["loc"].min(), 2))
print(f"Máximo:", round(jm1_data["loc"].max(), 2))
print(f"Amplitude:", round(jm1_data["loc"].max() - jm1_data["loc"].min(), 2))
print(f"Variância:", round(jm1_data["loc"].var(), 2))
print(f"Desvio-padrão:", round(jm1_data["loc"].std(), 2))