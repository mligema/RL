
import numpy as np
import matplotlib.pyplot as plt
import csv
from pprint import pprint
#from scikits.statsmodels.tools import categorical
import pandas as pd

arr = np.empty((0,3), dtype=object)
'''
row_num = 0
with open('PlantGrowth.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        row_num += 1

        if row_num == 1:
            header = row
            continue
        #arr.(row)
'''

#arr = np.vstack((arr, np.array([4,5,6])))
#arr = np.vstack((arr, np.array([5,6,7])))
row_num = 0
with open('PlantGrowth.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        row_num += 1
        if row_num == 1:
            header = row
            continue
        arr = np.vstack((arr, np.array(row)))

print(arr)

dummies = pd.get_dummies(arr[:, -1])

print(arr[:, -1])
print(dummies.values.argmax(1))

arr[:, -1] = dummies.values.argmax(1)

print(arr)

arr_float = arr.astype(np.float)

print('*')
print(arr_float[:, -2:])
print('*')
'''
row_num = 0
with open('PlantGrowth.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        row_num += 1

        if row_num == 1:
            header = row
            continue
        np_array.vstack(row)

print(header)
print(type(header))
print(np_array)'''

'''
import numpy as np
a = np.array([[1,3,4],[1,2,3],[1,2,1]])
b = np.array([10,20,30])
c = np.hstack((a, np.atleast_2d(b).T))
d = np.vstack((a, np.atleast_2d(b)))

print(a)
print(b)
print(c)
print(d)
'''
#a = np.genfromtxt('PlantGrowth.csv', delimiter=',', skip_header=True)
#a = np.random.uniform(0, 10, [100, 5])

#pprint(a)

plt.boxplot()
plt.show()
