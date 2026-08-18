from __init__ import reduced_software_project_risk_data

import pandas as pd

data = reduced_software_project_risk_data

"""
Divida os projetos em grupos de acordo com o nível de risco existente no conjunto de dados. 

Compare as médias das duas variáveis selecionadas entre os grupos. 
"""

data["Risk_Level"] = pd.cut(
    data["Risk_Score"], bins=3, labels=["Low", "Medium", "High"]
)

result = data.groupby("Risk_Level", observed=True)[
    ["Estimated_Effort_Hours", "Actual_Effort_Hours"]
].agg(["mean", "std"])

print(result)
