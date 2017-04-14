import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

datafile = 'PlantGrowth.csv'
data = pd.read_csv(datafile)
data.head()

data.boxplot('weight', by='group')
plt.show()

grps = pd.unique(data.group.values)
d_data = {grp:data['weight'][data.group == grp] for grp in grps}
k= len(pd.unique(data.group))
N = len(data.values)
n = data.groupby('group').size()[0]

f, p = stats.f_oneway(d_data['ctrl'], d_data['trt1'], d_data['trt2'])
print('f =', f, 'p =', p)

ss_between = (sum(data.groupby('group').sum()['weight']**2)/n) - (data['weight'].sum()**2)/N
sum_y_squared = sum([value**2 for value in data['weight'].values])

ss_within = sum_y_squared - sum(data.groupby('group').sum()['weight']**2)/n
ss_total = sum_y_squared - (data['weight'].sum()**2)/N

# degrees of freedom
df_between = k - 1
df_within = N - 1
df_total = N - 1

# Mean square
ms_between = ss_between/df_between
ms_within = ss_within/df_within

# calculating the f-ration
f = ms_between/ms_within

# lets get a p-value
p = stats.f.sf(f, df_between, df_within)
# effect sizes
ets_squared = ss_between/ss_total
omega_squared = (ss_between - (df_between * ms_within))/(ss_total + ms_within)

print('f =', f, 'p =', p, 'ets_squared =',  ets_squared, 'omega_squared =', omega_squared)




