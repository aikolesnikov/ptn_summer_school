import pandas as pd
import matplotlib.pyplot as plt

ts = pd.read_csv('~/prog/pyt/data/GlobalLandTemperaturesByMajorCity.csv')

print(type(ts))
print(ts)
print(ts.count())
print(ts.head(10))
print(ts.tail(5))
print(ts.describe())
print()

print(ts['City'])
print(ts['City'].unique())
print(ts['City'].value_counts())
#print(ts['City','AverageTemperature'])
print()

print(ts['City'][:5])
print(ts.iloc[0][0])
print()

print(ts['City'].values)
print(ts['City'].values=='Kiev')
print(ts[ts['City'].values=='Kiev'])
#plt.plot(ts[ts['City'].values=='Kiev'])
plt.plot(ts.index, ts['AverageTemperature'])
plt.show()


