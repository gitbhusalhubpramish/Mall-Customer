from pathlib import Path
import kagglehub
import pandas as pd

path = kagglehub.dataset_download("shwetabh123/mall-customers")

df = pd.read_csv(path)

