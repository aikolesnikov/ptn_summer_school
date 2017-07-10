import numpy as np
import scipy.interpolate
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 20)
y = np.sin(x)

f = interp1d(x, y)
f1 = interp1d(x, y)
print(np.sin(5))
print(f(5))

plt.plot(x, f(x), '-', f1(x), '--')
#plt.show()

from scipy.stats import describe
print(describe(x))
