
#import pandas as pd
import numpy as np
#datafile = 'PlantGrowth.csv'

import matplotlib as mlp
import matplotlib.pyplot as plt

## agg backend is used to create plot as a .png file
#mlp.use('agg')

## Create data
np.random.seed(10)
collectn_1 = np.random.normal(100, 10, 200)
collectn_2 = np.random.normal(80, 30, 200)
collectn_3 = np.random.normal(90, 20, 200)
collectn_4 = np.random.normal(70, 25, 200)

## combine these different collections into a list
data_to_plot = [collectn_1, collectn_2, collectn_3, collectn_4]

#print(data_to_plot[0])
#print(type(data_to_plot[0]))

# Create a figure instance
fig = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig.add_subplot(111)

# Create the boxplot
bp = ax.boxplot(data_to_plot)

# Save the figure
#fig.savefig('fig1.png', bbox_inches='tight')
fig.show()

#data = pd.read_csv(datafile)

#print(data.head())
#print(data[['weight', 'group']].as_matrix().T)
#print(type(data.as_matrix()))

#print(np.random.normal(100, 10, 200))

#plt.boxplot(data[['weight', 'group']].as_matrix().T)
#plt.show()

#print(data['weight'])
#print(type(data['weight']))

#plt.boxplot(x=data['weight'], )
#plt.show()

#print(data.head())

#print(data[['weight', 'group']].head())

# visualize with boxplot

#plt.boxplot(data)
#plt.show()

#grouped = data['weight'].groupby(axis=1, level='gruop').T

#print(grouped)
