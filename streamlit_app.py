from pathlib import Path
import numpy as np
import kagglehub
import pandas as pd
import streamlit as st

path = kagglehub.dataset_download("shwetabh123/mall-customers", path="Mall_Customers.csv")

df = pd.read_csv(path)

st.write('''## Raw data''')
st.scatter_chart(df, x="Annual Income (k$)", y = "Spending Score (1-100)")

st.write('''Here the data seems like it is divided into 5 groups so our k will be 5. These kind of data are perfect for k-means''')

k = 5

cen = pd.DataFrame(df.drop(columns=["CustomerID"]).sample(random_state=42))

st.write(cen.dtype())
st.write(df.dtype())

for i in range(k-1):
	dx = abs((cen.apply(lambda c: np.sqrt(((df.drop(columns=["CustomerID"])-c)**2).sum(axis-1)), axis=1))).T.min(axis=1)
	p = dx/dx.sum()
	cen.loc[i+1] = df.drop(columns=["CustomerID"]).iloc[np.argmax(p)]


st.write('''## Initial centroid after K-means++''')
st.scatter_chart(cen, x="Annula Income (k$)", y = "Spending score (1-100)")

