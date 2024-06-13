import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score

from sklearn.ensemble import RandomForestClassifier  
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

df = pd.read_csv("data.csv")
df.tail()

#Removing Null values
update_df = df.drop([199, 200, 201,202])
update_df.shape
update_df.isnull().sum()

x = update_df.iloc[:,[0,1,2,3,4]].values
print(x)

wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters = i,init = 'k-means++', random_state = 0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

#plot elbow graph
sns.set()
plt.plot(range(1,11), wcss)
plt.title('WCSS - within-cluster-sum-of-square')
plt.xlabel('No. of clusters')
plt.ylabel('WCSS')
plt.show()

#Optimum no. of cluster is 2
kmeans = KMeans(n_clusters = 2,init = 'k-means++', random_state = 0)

y = kmeans.fit_predict(x)
print(y)

#scater plot
#visualiszing ploting
plt.figure(figsize = (8,8))
plt.scatter(x[y == 0,0], x[y == 0,1], s = 50, c= 'yellow', label ='C1')
plt.scatter(x[y == 1,0], x[y == 1,1], s = 50, c= 'blue', label ='C2')
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s= 100, c='green', label ='Centroid')
plt.show()
sns.heatmap(update_df.corr(),annot=True)
plt.show()

classifier= RandomForestClassifier(n_estimators= 10, criterion="entropy")
classifier.fit(x,y)
ypred= classifier.predict(x)
ypred

accuracy_score(y, ypred)

current = 5.1
voltage = 229
temperature = 65.23
humidity = 68
vibration = 0
test = [[current, voltage, temperature, humidity, vibration]]


def give_pred(test):
    prediction = classifier.predict(test)

    if prediction != 0:
        return ('Your System Works')
    return ('Your System Failed')

print(give_pred(test))
