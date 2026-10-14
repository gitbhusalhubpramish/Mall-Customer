from pathlib import Path
import kagglehub
import pandas as pd
import streamlit as st

path = kagglehub.dataset_download("shwetabh123/mall-customers", path="Mall_Customers.csv")

df = pd.read_csv(path)

st.write('''## Raw data''')
st.scatter_chart(df["Annual Income (k$)"], df["Spending Score (1-100)"])

st.write('''Here the data seems like it is divided into 5 groups so our k will be 5. These kind of data are perfect for k-means''')

k = 5

