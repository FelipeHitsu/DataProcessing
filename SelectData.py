import numpy as np
import pandas as pd

from pandas import Series,DataFrame

dados = np.arange(8)
dados.reshape((4, 2))


indice = ['linhas 1','linhas 2','linhas 3','linhas 4',
          'linhas 5','linhas 6','linhas 7','linhas 8']

serie = Series(dados, index = indice)
serie

print(serie['linhas 6'])
np.random.seed(25)
linhas = ['linha 1','linha 2','linha 3','linha 4','linha 5','linha 6']
colunas = ['coluna 1','coluna 2','coluna 3','coluna 4','coluna 5','coluna 6']

df  = DataFrame(np.random.rand(36).reshape((6,6)),
                index = linhas,
                columns= colunas)
print(df)
print('')
print(df.loc[['linha 2','linha 4'],['coluna 3','coluna 5']])


