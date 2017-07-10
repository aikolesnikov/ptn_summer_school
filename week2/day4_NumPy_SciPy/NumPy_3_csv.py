import csv
import numpy as np

f = open('csv_example.csv', 'rt')
r = csv.reader(f)
for row in r:
    print(row)
f.close()
print()

with open('csv_example.csv', 'rt') as f:
    r = csv.reader(f)
    for row in r:
        print(row)

from_csv = np.genfromtxt('csv_example.csv', dtype=None, delimiter=',')
print(from_csv)
print(from_csv[0][1])