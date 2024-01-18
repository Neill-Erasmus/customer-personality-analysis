import numpy
import matplotlib.pyplot as plt
import pandas

dataset = pandas.read_csv('data/customer_segmentation.csv')
X = dataset.iloc[:, [col for col in range(dataset.shape[1]) if (col != 0) and (col != 7)]].values

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [1, 2])], remainder='passthrough')
X = numpy.array(ct.fit_transform(X))

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=numpy.nan, strategy='mean')
X[:,:] = imputer.fit_transform(X[:,:])

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=4, init='k-means++', random_state=42)
y_kmeans = kmeans.fit_predict(X=X)

from sklearn.metrics import silhouette_score
silhouette_avg = silhouette_score(X, y_kmeans)
print(f"Silhouette Score: {silhouette_avg}")

from sklearn.metrics import calinski_harabasz_score
calinski_harabasz = calinski_harabasz_score(X, y_kmeans)
print(f"Calinski-Harabasz Index: {calinski_harabasz}")

from sklearn.metrics import davies_bouldin_score
davies_bouldin = davies_bouldin_score(X, y_kmeans)
print(f"Davies-Bouldin Index: {davies_bouldin}")

import joblib
joblib.dump(kmeans, 'model/model.joblib')