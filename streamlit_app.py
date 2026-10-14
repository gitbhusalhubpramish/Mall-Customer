from pathlib import Path
import kagglehub
import pandas as pd

path = kagglehub.dataset_download("shwetabh123/mall-customers", path="Mall_Customers.csv")

df = pd.read_csv(path)

