"""Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего
из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без
get_dummies?

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
"""

import pandas as pd
from random import shuffle

lst = ['robot'] * 10
lst += ['human'] * 10
shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data['human'] = ''                                         # Future warning
data['robot'] = ''
data.loc[data['whoAmI'] == 'human', 'human'] = True
data.loc[data['whoAmI'] != 'human', 'human'] = False
data.loc[data['whoAmI'] == 'robot', 'robot'] = True
data.loc[data['whoAmI'] != 'robot', 'robot'] = False
print(data.head())


"""Второе решение

import pandas as pd
from random import shuffle

lst = ['robot'] * 10
lst += ['human'] * 10
shuffle(lst)
human_list = (True if el == 'human' else False for el in lst)
robot_list = (True if el == 'robot' else False for el in lst)
data = pd.DataFrame({'whoAmI_human':human_list,'whoAmI_robot':robot_list})
print(data)
"""