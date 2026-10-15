# Mall Customer with K-means

In this project I have applied K-means from scratch in [Mall Customer](https://www.kaggle.com/datasets/shwetabh123/mall-customers) dataset in kaggle. This markdown is just the overview of the project I have given more details in my [notes](https://github.com/gitbhusalhubpramish/ml-notes/tree/main/0.008%20K-means).

<img src="visula.jpg"/>

This image is just the final result after the clustering the data. [Click here](https://mall-customer-pramish-bhusal.streamlit.app/) to see full anylais of the dataset.

## Small intro to K-means

K-means is a unsupervised clustring meachine learning algorithm. Means it doesn't have a label or doesn't have to predict the output rather clusterize the data, find patterns. We select some points called centroid and optmize them so all points are at minimum distance from it's centroid.

## Feature

This project was made by me to understand K-means from scratch so it's main fearture is it has K-means applied from scratch but also:

- K-means form scratch
- K-means++ for centroid initlization
- Numpy for math and matrix calculation
- pandas for data manipulation
- Data visulization
- Clusters data 

## Tech-Stack

This project uses python liberies used for data science - visulization, caculation and data manipulation. I've used:

- Numpy for math and matrix calculation.
- matplotlib and streamlit for datavisulization
- pandas for csv and data manipulation.

## Work-flow

The work flow of the project look like this:

- **Fetch data:** Here it fetches the data from kaggle dataset.
- **K-means++ for centroid initlization:** Here first centroid is initlized randomly. Then, K-means++ uses distance and probability to calculate next centroid - it chooses the furtherest point.
- **Centroid centroization:** Here centorid is keept in the center of it's cluster.
- **Clustring:** Here every datapoint is clusterized with the nearest centroid.
- **Visulization:** Here we visulize the data after clustering in a scatter chart to conform whether it works well.

## What did I learn?

I had made this project to learn K-means form scratch. Ofcource I had learnt that. But others too like:

- K-means
- Clustring
- Data visulization

## Some extra info...

I have been learning Meachine Learning so I make notes and make atleast one poject for each. I have writtern a jupiter notebook to plan and make this work then I make a python script file with the help of streamlit so that I can host and support Hackclub. Most of the progress is in my notebook. I made this to learn so it has very less AI implimented. I know how it works and why this works. A lot of time was spent in visulization and logic building which wasn't track by hackatime
