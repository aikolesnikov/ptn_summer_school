import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn import datasets

iris = datasets.load_iris()
print(iris)
print('-----------')

features = iris.data
print(features)
print(len(features))

