import numpy as np
import numpy.random
import matplotlib.pyplot as plt

# import matplotlib.pyplot as plt


print(np.arange(1, 10))
x = np.linspace(0, 10, 30)
print(x)
y = x * 2
print(y)
print(np.amin(y))

a = np.random.rand(2, 3)
print(a)
print(np.amin(a, axis=0))
print(np.amin(a, axis=1))
print(np.amax(a, axis=0))

a[0][0] = None
print(np.amin(a))
print(a)
print(np.nanmin(a))
print(np.nanmax(a))
print()

print(a[0, 1])
print(a[0, :])
print(a[:, 0])
print(a[:, [0, 2]])
print(np.nanmin(a) - np.nanmax(a))
print()

print(np.nanpercentile(a, 25))
b = np.random.rand(100, 100)
print(np.percentile(b, 25))
print()

print(np.nanmean(a))
print(np.nanmean(b))

a[0, 0] = 1000
print(np.nanmean(a))
print

s = np.random.normal(0, 1, 100)
print(s)
print(np.histogram(s))
plt.plot(np.histogram(s)[0])
# plt.show()
print()

x = np.linspace(0, 10, 40)
print(x)
print(np.corrcoef(x, x ** 2))
print(np.corrcoef(x, np.sin(x)))
