import numpy as np
import numpy.random

'''
a1 = np.ndarray([1,2,3])
print(a1)
# Ellipsis

a1 = np.random.rand(1,3)
print(a1)
print()
'''

a1 = np.random.rand(2, 3)
print(a1)
print('type', a1.dtype)
print('size', a1.shape)

print(a1.reshape((3, 2)))
print(a1.T)
print()
print(a1 + 4)
print(a1 ** 4)
print(np.sin(a1))
print()

b1 = np.random.rand(2, 3)
print(b1)
print(a1 + b1)
print(a1.dot(b1.T))

a1 = a1 * 10
print(a1)
print(a1 > 4)
m = a1 > 4
print(a1[m])
print(b1[m])

for i in a1.flat:
    print(i)
print()



