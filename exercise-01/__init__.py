import os
import pandas as pd

path = os.getcwd()

jm1_data = pd.read_csv(f"{path}\\exercise-01\\archive\\jm1.csv")
reduced_software_project_risk_data = pd.read_csv(
    f"{path}\\exercise-01\\archive\\Reduced_Software_Project_Risk_Dataset_585.csv"
)
