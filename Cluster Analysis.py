# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 22:36:17 2020
Cluster Analysis
@author: anthe
"""
import os
import pandas as pd 
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

'''Ready and prepare data'''
os.chdir('C:\\Users\\anthe\\Documents\\GitHub\\Incel') 
df = pd.read_csv(r'Ready.csv') 
df=df.drop(['Unnamed: 0'], axis=1) 
summary=np.transpose(df.describe())
#43302 text pieces remain

#Scale data so that the features have a mean of 0 and standard deviation of 1
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df)

'''Finding the number of clusters'''
from kneed import KneeLocator
from sklearn.metrics import silhouette_score

'''Elbow Method'''
kmeans_kwargs = {
     "init": "random",
     "n_init": 10,
     "max_iter": 300,
     "random_state": 42,
 }

# A list holds the SSE values for each k
sse = []
for k in range(1, 11):
     kmeans = KMeans(n_clusters=k, **kmeans_kwargs)
     kmeans.fit(scaled_features)
     sse.append(kmeans.inertia_)
plt.style.use("fivethirtyeight")
plt.plot(range(1, 11), sse)
plt.xticks(range(1, 11))
plt.xlabel("Number of Clusters")
plt.ylabel("SSE")
plt.show()   
     
#Find the elbow
kl = KneeLocator(range(1, 11), sse, curve="convex", direction="decreasing")

kl.elbow
#4 clusters

'''Silhouette Method'''
# A list holds the silhouette coefficients for each k
silhouette_coefficients = []
# Notice you start at 2 clusters for silhouette coefficient
for k in range(2, 11):
     kmeans = KMeans(n_clusters=k, **kmeans_kwargs)
     kmeans.fit(scaled_features)
     score = silhouette_score(scaled_features, kmeans.labels_)
     silhouette_coefficients.append(score)
     
plt.style.use("fivethirtyeight")
plt.plot(range(2, 11), silhouette_coefficients)
plt.xticks(range(2, 11))
plt.xlabel("Number of Clusters")
plt.ylabel("Silhouette Coefficient")
plt.show()     
#suggests 2 clusters!     
     

'''Perform the Analysis'''

'''2 Clusters'''
kmeans = KMeans(
     init="random",
     n_clusters=2,
     n_init=10,
     max_iter=300,
     random_state=42
)

kmeans.fit(scaled_features)
y_kmeans = kmeans.predict(scaled_features)
# The lowest SSE value- inertia calculates the sum of distances of all the points within a cluster from the centroid of that cluster
kmeans.inertia_
# The number of iterations required to converge
kmeans.n_iter_

# plot the 2 clusters

plt.scatter(
    scaled_features[y_kmeans == 0, 0], scaled_features[y_kmeans == 0, 1],
    s=50, c='lightgreen', marker='s', edgecolor='black',
    label='cluster 1'
)

plt.scatter(
    scaled_features[y_kmeans == 1, 0], scaled_features[y_kmeans == 1, 1],
    s=50, c='orange', marker='o', edgecolor='black',
    label='cluster 2'
) 
# plot the centroids
plt.scatter(
    kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
    s=250, marker='*',
    c='red', edgecolor='black',
    label='centroids'
)
plt.legend(scatterpoints=1)
plt.grid()
plt.show()


groups=pd.DataFrame(y_kmeans)
groups=groups.rename(columns={0: "Groups"})
df2=pd.concat([df, groups], axis=1, sort=False)
groups_agg = df2.groupby("Groups", as_index=True).agg("mean") 
groups_agg['Count']=df2.Groups.value_counts()
groups_agg.to_csv('C:\\Users\\anthe\\Documents\\GitHub\\Incel\\2 Clusters\\2 Cluster Solution.csv')

'''4 Clusters'''
kmeans4 = KMeans(
     init="random",
     n_clusters=4,
     n_init=10,
     max_iter=300,
     random_state=42
)

kmeans4.fit(scaled_features)
y_kmeans4 = kmeans4.predict(scaled_features)
# The lowest SSE value- inertia calculates the sum of distances of all the points within a cluster from the centroid of that cluster
kmeans4.inertia_
# The number of iterations required to converge
kmeans4.n_iter_
# Final locations of the centroid
centers=pd.DataFrame(kmeans4.cluster_centers_)
centers.columns=list(df.columns) 
centers.to_csv('C:\\Users\\anthe\\Documents\\GitHub\\Incel\\4 Clusters\\4 Cluster Centers.csv')

plt.scatter(
    scaled_features[y_kmeans4 == 0, 0], scaled_features[y_kmeans4 == 0, 1],
    s=15, c='lightgreen', marker='s', edgecolor='black',
    label='cluster 1'
)

plt.scatter(
    scaled_features[y_kmeans4 == 1, 0], scaled_features[y_kmeans4 == 1, 1],
    s=15, c='orange', marker='o', edgecolor='black',
    label='cluster 2'
) 

plt.scatter(
    scaled_features[y_kmeans4 == 2, 0], scaled_features[y_kmeans4 == 2, 1],
    s=15, c='blue', marker='o', edgecolor='black',
    label='cluster 3'
) 
plt.scatter(
    scaled_features[y_kmeans4 == 3, 0], scaled_features[y_kmeans4 == 3, 1],
    s=15, c='purple', marker='h', edgecolor='black',
    label='cluster 4'
)  
# plot the centroids
plt.scatter(
    kmeans4.cluster_centers_[:, 0], kmeans4.cluster_centers_[:, 1],
    s=25, marker='*',
    c='red', edgecolor='black',
    label='centroids'
)
plt.legend(scatterpoints=1)
plt.grid()
plt.show()

#Get means aggregated by group
groups=pd.DataFrame(y_kmeans4)
groups=groups.rename(columns={0: "Groups"})
df4=pd.concat([df, groups], axis=1, sort=False)
groups_agg4 = df4.groupby("Groups", as_index=True).agg("mean")
groups_agg4['Count']=df4.Groups.value_counts()
groups_agg4.to_csv('C:\\Users\\anthe\\Documents\\GitHub\\Incel\\4 Clusters\\4 Cluster Solution.csv')

#Add group label to original data
df = pd.read_csv(r'C:\\Users\\anthe\\Documents\\GitHub\\Incel\\Ready2.csv') 
df4=pd.concat([df, groups], axis=1, sort=False) 
df4.to_csv('C:\\Users\\anthe\\Documents\\GitHub\\Incel\\4 Clusters\\Grouped Data.csv')
