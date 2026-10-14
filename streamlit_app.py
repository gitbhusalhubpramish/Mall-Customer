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

df["Genre"] = df["Genre"].map({"Male":1, "Female":0})

k = 5

cen = pd.DataFrame(df.drop(columns=["CustomerID"]).sample(random_state=42))

st.write(cen.dtypes)
st.write(df.dtypes)

for i in range(k-1):
	dx = abs((cen.apply(lambda c: np.sqrt(((df.drop(columns=["CustomerID"])-c.to_numpy())**2).sum(axis=1)), axis=1))).T.min(axis=1)
	p = dx/dx.sum()
	cen.loc[i+1] = df.drop(columns=["CustomerID"]).iloc[np.argmax(p)]


st.write('''## Initial centroid after K-means++''')
st.scatter_chart(cen, x="Annual Income (k$)", y = "Spending Score (1-100)")

def train():
	global cen
	dx = np.argmin(abs((cen.apply(lambda c: np.sqrt(((df.drop(columns=["CustomerID"])-c.to_numpy())**2).sum(axis=1)), axis=1))).T, axis=1)
	c = pd.Series(dx).groupby(dx).apply(lambda x:x.index.tolist())
	csum = df.drop(columns=["CustomerID"]).groupby(dx).sum()
	cen = csum.div(c.str.len(), axis=0)

def loss():
	dx = np.argmin(abs((cen.apply(lambda c: np.sqrt(((df.drop(columns=["CustomerID"])-c.to_numpy())**2).sum(axis=1)), axis=1))).T,axis=1)
	c = pd.Series(dx).groupby(dx).apply(lambda x: x.index.tolist())
	return np.sum(np.sum(np.sqrt((cen.iloc[0]-df.drop(columns=["CustomerID"]).iloc[c.iloc[0]])**2), axis=1))

def cat():
	dx = np.argmin(abs((cen.apply(lambda c:np.sqrt(((df.drop(colunms=["CustomerID"])-c.to_numpy())**2).sum(axis=1)), axis=1))).T, axis=1)
	return pd.Series(dx).groupby(dx).apply(lambda x:x.index.tolist()).apply(lambda p: df.iloc[p])

losses = [loss()]

for i in range(10):
	train()
	losses.append(loss())

