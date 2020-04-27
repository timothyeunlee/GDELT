import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler 
import seaborn as sns
import matplotlib.pyplot as plt
import cmath as math

# Tutorial: https://heartbeat.fritz.ai/k-means-clustering-using-sklearn-and-python-4a054d67b187


# read in the csv 
coverage = pd.read_csv("./most_coverage/most_coverage.csv")
# print(coverage)
X = coverage.iloc[:,[0,1,2,3]].values # NumCoverage, Num Articles, Num Mentions 

# Finding the Optimal Amount of Clusters 
Sum_of_squared_distances = []
K = range(1,15)
for k in K:
    km = KMeans(n_clusters=k)
    km = km.fit(coverage)
    Sum_of_squared_distances.append(km.inertia_)

plt.plot(K, Sum_of_squared_distances, 'bx-')
plt.xlabel('k')
plt.ylabel('Sum_of_squared_distances')
plt.title('Elbow Method For Optimal k')
plt.show()

# From plot we can see optimal K is 3 
# Using the sklearn library to do clustering 
kmeans = KMeans(n_clusters = 3)
y_kmeans = kmeans.fit_predict(X)

print(y_kmeans)

print(kmeans.cluster_centers_)

# Prints out the clusters  
plt.scatter(X[:,0], X[:, 1], c = y_kmeans, cmap='rainbow')
plt.title('Most Coverage')
plt.show()