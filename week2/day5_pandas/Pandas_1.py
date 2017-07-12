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
# print(ts['City','AverageTemperature'])
print()

print(ts['City'][:5])
print(ts.iloc[0][0])
print()

print(ts['City'].values)
print(ts['City'].values == 'Kiev')
print(ts[ts['City'].values == 'Kiev'])
print(ts[ts['City'].values == 'Kiev'].dropna())

plt.plot(ts.index, ts['AverageTemperature'])
ds2 = ts[ts['City'] == 'Kiev'].dropna()
plt.plot(ds2.index, ds2['AverageTemperature'])
#plt.show()


### -------------------------------------------
ts = pd.read_csv('~/prog/pyt/data/GlobalLandTemperaturesByMajorCity.csv', parse_dates=['dt'])
print(ts)

tsk = ts[ts['City'] == 'Kiev']
print(tsk.count())
print(ts['dt'])

tsk = tsk.interpolate()
tsk['year'] = tsk['dt'].dt.year
print(tsk)
tsk.groupby('year')
print(type(tsk.groupby('year')))