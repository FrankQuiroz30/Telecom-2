# Librerias ---------------------------------------- 

import pandas as pd
import os, sys
sys.path.append(os.getcwd()) 
# Esto es para agregar al path la ruta de ejecución actual y poder importar respecto a la ruta del proyecto, desde donde se debe ejecutar el código


# Loading data ---------------------------------------- 
contract_raw = pd.read_csv("datasets/contract.csv")
internet_raw = pd.read_csv("datasets/internet.csv")
personal_raw = pd.read_csv("datasets/personal.csv")
phone_raw = pd.read_csv("datasets/phone.csv")

# Cleaning columns ---------------------------------------- 

# Eliminating duplicates per period ---------------------------------------- 

# ...

# Checking NAs ---------------------------------------- 

# ...

# Guardar datos ---------------------------------------- 

users_behavior.to_csv("files/datasets/intermediate/a01_users_behavior_cleaned.csv", index=False)


