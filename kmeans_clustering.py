import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df=pd.read_csv('/content/Mall_Customers.csv')
df.head()
df.info()

df['Genre']=df['Genre'].map({'Male':1,'Female':0})

x=df[['Age','Spending_Score']]

wcss=[]
for i in range(1,11):
  kmeans=KMeans(n_clusters=i,init='k-means++',random_state=42)
  kmeans.fit(x)
  wcss.append(kmeans.inertia_)
plt.figure(figsize=(10,5))
plt.plot(range(1,11),wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

kmeans=KMeans(n_clusters=5,init='k-means++',random_state=42)
y=kmeans.fit_predict(x)

print(kmeans.inertia_)

print(kmeans.labels_)

plt.scatter(x[y==0]['Age'],x[y==0]['Spending_Score'],color='red',label='cluster1',s=30)
plt.scatter(x[y==1]['Age'],x[y==1]['Spending_Score'],color='yellow',
label='cluster2',s=30)
plt.scatter(x[y==2]['Age'],x[y==2]['Spending_Score'],color='green',label='cluster3',s=30)
plt.scatter(x[y==3]['Age'],x[y==3]['Spending_Score'],color='blue',label='cluster4',s=30)
plt.scatter(x[y==4]['Age'],x[y==4]['Spending_Score'],color='grey',label='cluster5',s=30)
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],color='pink',label='Centroid',s=100)
plt.title('KMeans Clustering')
plt.xlabel('Age')
plt.ylabel('Spending_Score')
plt.legend()
plt.show()
