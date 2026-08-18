from __init__ import jm1_data

# Etapa 1 - Conhecimento dos dados

'''
Quantidade de registros; 
Quantidade de variáveis; 
Nome das variáveis; 
Tipo de cada variável; 
Variável relacionada à ocorrência de defeito; 
Existência de valores ausentes. 
'''
print(len(jm1_data))
print()
print(len(jm1_data.columns.to_list()))
print()
jm1_data.info()
print()
print(jm1_data["defects"].value_counts())
print()
print(jm1_data.isnull().sum())