import numpy as np
import pandas as pd

#series

dic = {'a':10, 'b':20}
s = pd.Series(dic)
s2 = pd.Series(data=[20,30,40],index = ['a', 'b','d'])
print(s)


#dataframes