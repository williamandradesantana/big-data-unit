from __init__ import reduced_software_project_risk_data

data = reduced_software_project_risk_data

"""
Número de projetos; 
Número de variáveis; 
Variáveis quantitativas; 
Variáveis qualitativas; 
Variável relacionada ao risco. 
"""

print("Número de projetos:", len(data["Project_Size"]))
print("Número de variáveis:", len(data.columns))
print("Variáveis quantitativas:", data.select_dtypes("number").columns.tolist())
print("Variáveis qualitativas:", data.select_dtypes(exclude="number").columns.tolist())
print("Variável relacionada ao risco: Risk_Score")
