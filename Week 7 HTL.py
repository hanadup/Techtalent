K-Means clustering

K-means clustering is an unsupervised machine learning algorithm. In K-means data objects are separated into groups/clusters which closely align with other data objects in the same group and not from other groups/clusters. A number of centroids are assigned to the data which corresponds to the amount groups or clusters the operator has chosen. The distance between the centroids and each data objects are calculated, and the data objects are assigned to the nearest centroid, the mean position of each data objects assigned to the centroid is calculated and this is used to update the centroid position and this process keeps going until the centroid position doesn’t update anymore and the centroids are in their final position. 
This algorithm would be useful for customer segmentation to group customers into different groups to identify customers which are suited for the marketing a certain new products from a large amount of unlabelled customer data that are more likely to buy the new product.
This algorithm is widely used in banks to detect fraudulent transactions from previous data of their customers (i.e. purchase habits, transaction amount, purchase frequency and etc) if an anomaly purchase is detected and is not similar to past purchases verification from the customers is requested to ensure that the purchase is genuine by that customer otherwise the purchase will not go through and will be rejected by the bank, also the credit/debit card may be frozen until further notice.


Optional HLT

from ast import increment_lineno
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
dataset = pd.read_csv(r"C:\Users\hanad\Desktop\Coding\Data Academy (Tech talent)\student_scores.csv")
dataset.shape
dataset.head()
dataset.describe()
dataset.plot(x='Hours', y='Scores', style='o')
plt.title('Hours vs Percentage')
plt.xlabel('Hours Studied')
plt.ylabel('Percentage Score')
plt.show()
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
print(regressor.intercept_)
print(regressor.coef_)
y_pred = regressor.predict(X_test)
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df)
from sklearn import metrics
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
