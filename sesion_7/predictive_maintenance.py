import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Mount Google Drive if you're using Colab to access files
from google.colab import drive
drive.mount('/content/drive')

# Class for loading and cleaning data
class DataProcessor:
    def __init__(self, filename):
        self.df = pd.read_csv(filename)

    def clean_data(self):
        # Removing specific rows with null values
        self.df = self.df.drop([199, 200, 201, 202])
        return self.df

    def get_features(self):
        # Selecting specific columns as features
        return self.df.iloc[:, [0, 1, 2, 3, 4]].values

# Class for performing KMeans clustering
class KMeansProcessor:
    def __init__(self, data):
        self.data = data

    def find_optimal_clusters(self):
        wcss = []
        # Finding within-cluster sum of squares for different number of clusters
        for i in range(1, 11):
            kmeans = KMeans(n_clusters=i, init='k-means++', random_state=0)
            kmeans.fit(self.data)
            wcss.append(kmeans.inertia_)
        return wcss

    def perform_clustering(self, num_clusters):
        # Performing KMeans clustering with specified number of clusters
        kmeans = KMeans(n_clusters=num_clusters, init='k-means++', random_state=0)
        self.kmeans_model = kmeans.fit(self.data)
        return self.kmeans_model.labels_

# Class for visualization operations
class Visualization:
    @staticmethod
    def scatter_plot(x, y, kmeans):
        # Scatter plot of clustered data points and centroids
        plt.figure(figsize=(8, 6))
        plt.scatter(x[y == 0, 0], x[y == 0, 1], s=50, c='yellow', label='C1')
        plt.scatter(x[y == 1, 0], x[y == 1, 1], s=50, c='blue', label='C2')
        plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=100, c='green', label='Centroid')
        plt.legend()
        plt.title('KMeans Clustering')
        plt.xlabel('Feature 1')
        plt.ylabel('Feature 2')
        plt.grid(True)
        plt.show()

    @staticmethod
    def heatmap(df):
        # Heatmap visualization of correlation matrix
        plt.figure(figsize=(10, 8))
        sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=.5)
        plt.title('Correlation Heatmap')
        plt.show()

# Class for RandomForestClassifier operations
class RandomForestProcessor:
    def __init__(self, x, y):
        # Initializing RandomForestClassifier
        self.classifier = RandomForestClassifier(n_estimators=10, criterion="entropy", random_state=0)
        self.classifier.fit(x, y)

    def predict(self, test):
        # Predicting using trained classifier
        return self.classifier.predict(test)

    def accuracy(self, y, y_pred):
        # Calculating accuracy score
        return accuracy_score(y, y_pred)

def main():
    # Specify the path to your data file in Google Drive
    filename = '/content/drive/My Drive/data.csv'

    # Initialize DataProcessor to load and clean data
    data_processor = DataProcessor(filename)
    cleaned_data = data_processor.clean_data()
    features = data_processor.get_features()

    # Initialize KMeansProcessor for clustering
    kmeans_processor = KMeansProcessor(features)
    wcss = kmeans_processor.find_optimal_clusters()
    num_clusters = 2
    y_clusters = kmeans_processor.perform_clustering(num_clusters)

    # Visualize clustered data
    Visualization.scatter_plot(features, y_clusters, kmeans_processor.kmeans_model)

    # Visualize correlation heatmap of cleaned data
    Visualization.heatmap(cleaned_data)

    # Initialize RandomForestProcessor for classification
    random_forest = RandomForestProcessor(features, y_clusters)

    # Test data for prediction
    test_data = np.array([[5.1, 229, 65.23, 68, 0]])

    # Predict using RandomForestClassifier
    prediction = random_forest.predict(test_data)
    accuracy = random_forest.accuracy(y_clusters, random_forest.predict(features))
    print("Prediction:", prediction)
    print("Accuracy:", accuracy)

    # Function to predict based on classifier
    def give_pred(test):
        prediction = random_forest.predict(test)
        if prediction != 0:
            return 'Your System Works'
        return 'Your System Failed'

    # Test prediction function
    print(give_pred(test_data))

if __name__ == "__main__":
    main()
