import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

### -------------------------------------------
ts0 = pd.read_csv('~/prog/pyt/data/GlobalLandTemperaturesByCountry.csv', parse_dates=['dt'])

tsk3 = ts0.dropna().groupby('Country')['AverageTemperature'].aggregate(np.median).sort_values()
print(tsk3.index)
ds2 = ts0[ts0['AverageTemperature'].values >= 22].dropna()
print(ds2)
tsk3.plot()
plt.show()

