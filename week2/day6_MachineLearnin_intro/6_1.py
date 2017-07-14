# import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn import datasets

iris = datasets.load_iris()
print('-----------')

features = iris.data
print(features)
print(len(features))

target = iris.target
print(target)

print(features[target == 0])
print(len(features[target == 0]))

#plt.scatter(features[target == 0, 0], features[target == 0, 1], marker='o')
#plt.scatter(features[target == 1, 0], features[target == 1, 1], marker='o')
#plt.scatter(features[target == 2, 0], features[target == 2, 1], marker='o')

plt.scatter(features[target == 0, 2], features[target == 0, 3], marker='o')
plt.scatter(features[target == 1, 2], features[target == 1, 3], marker='o')
plt.scatter(features[target == 2, 2], features[target == 2, 3], marker='o')

plt.show()

from sklearn.neighbors import KNeighborsClassifier
clr = KNeighborsClassifier(n_neighbors=3)



