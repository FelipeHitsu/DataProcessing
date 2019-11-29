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