from __init__ import data

# Etapa 1 - Conhecimento dos dados

'''
Quantidade de registros; 
Quantidade de variáveis; 
Nome das variáveis; 
Tipo de cada variável; 
Variável relacionada à ocorrência de defeito; 
Existência de valores ausentes. 
'''
print(len(data))
print()
print(len(data.columns.to_list()))
print()
data.info()
print()
print(data["defects"].value_counts())
print()
print(data.isnull().sum())