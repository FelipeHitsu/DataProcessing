import numpy as np
import pandas as pd

from pandas import Series,DataFrame

white_value = np.nan

serie = Series(['linha 1','linha 2',white_value,'linha 4','linha 5','linha 6',white_value,'linha 8'])

print(serie)
print('')

print(serie.isnull())
print('')

np.random.seed(25)
df = DataFrame(np.random.rand(36).reshape((6,6)))
print(df)
print('')

df.loc[3:5,0] = white_value
df.loc[1:4,5] = white_value
print(df)
print('')

df_process = df.fillna(0)
print(df_process)
print('')

dc = {0: 0.1,5: 1.25}
df_process = df.fillna(dc)
print(df_process)
print('')

#count and remove

