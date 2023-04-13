import pandas as pd
import numpy as np
from scipy.stats import *

chat_id = 680977959  # Ваш chat ID, не меняйте название переменной
# data1 = pd.read_table('historical_data.csv', sep=",", header=0, index_col=0)
# d1 = data1.to_numpy()
# data2 = pd.read_table('modified_data_of_type_3.csv', sep=",", header=0, index_col=0)
# d2 = data2.to_numpy()
#
# print(data1)
# print(d1)
# print(data2)
# print(d2)

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    sta, p = ttest_ind(x, y)
    return p < 0.09  # Ваш ответ, True или False

# t = 0
# f = 0
# for i in range(0, 100):
#     if(solution(d1[0], d1[i])):
#         t = t + 1
#     else:
#         f = f + 1
# print(t, f)