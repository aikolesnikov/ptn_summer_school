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

# plt.scatter(features[target == 0, 0], features[target == 0, 1], marker='o')
# plt.scatter(features[target == 1, 0], features[target == 1, 1], marker='o')
# plt.scatter(features[target == 2, 0], features[target == 2, 1], marker='o')

# better
# plt.scatter(features[target == 0, 2], features[target == 0, 3], marker='o')
# plt.scatter(features[target == 1, 2], features[target == 1, 3], marker='o')
# plt.scatter(features[target == 2, 2], features[target == 2, 3], marker='o')
plt.show()

from sklearn.neighbors import KNeighborsClassifier

clr = KNeighborsClassifier(n_neighbors=3)
print(clr.fit(features[1:], target[1:]))
print(clr.predict(features[0]))

from sklearn.cross_validation import KFold

kf = KFold(len(features), n_folds=5, shuffle=True)
print(kf)
for i in kf:
    print(i)

for training, testing in kf:
    clr.fit(features[training], target[training])
    print(np.mean(np.abs(clr.predict(features[testing]) == target[testing])))

print()
means = []
for training, testing in kf:
    clr.fit(features[training], target[training])
    means.append(np.mean(np.abs(clr.predict(features[testing]) == target[testing])))
    print(np.mean(means))

print()
for i in range(1, 20):
    for training, testing in kf:
        clr.fit(features[training], target[training])
        means.append(np.mean(np.abs(clr.predict(features[testing]) == target[testing])))
        print(np.mean(means))

print()
b = datasets.load_boston()
print(b)
features = b.data
target = b.target
from sklearn.linear_model import LinearRegression
r = LinearRegression()
r.fit(features[1:], target[1:])
print(r.predict(features[0]))
print(target[0])


