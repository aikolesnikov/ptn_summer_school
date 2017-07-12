import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
tsk.groupby('year')['AverageTemperature'].aggregate(min)
tsk.groupby('year')['AverageTemperature'].aggregate(max)
tsk.groupby('year')['AverageTemperature'].aggregate(np.median)
print(tsk.groupby('year')['AverageTemperature'].aggregate(np.median))

tsk2 = tsk.groupby('year')['AverageTemperature'].aggregate(np.median)
plt.plot(tsk2)
#plt.show()

def round_year(year):
    return year // 5 * 5;
print(round_year(2011))

tsk['year5'] = tsk['year'].apply(round_year)
print(tsk)
tskm = tsk.groupby('year5')['AverageTemperature'].aggregate(np.median)

f = np.poly1d(np.polyfit(tskm.index, tskm, 1))
print(f(2010))

plt.plot(tskm.index, f(tskm.index), 'x', tskm, '-')
#plt.show()


### -------------------------------------------
ts0 = pd.read_csv('~/prog/pyt/data/GlobalLandTemperaturesByCountry.csv', parse_dates=['dt'])

tsk3 = ts0.groupby('Country')['AverageTemperature'].aggregate(np.median)
print(tsk3.index)
print(tsk3)
tsk3.plot()
plt.show()
