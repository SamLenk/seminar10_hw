import pandas as pd

# Создаем исходный DataFrame
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print("Исходный DataFrame:")
print(data.head())

# Преобразуем столбец "whoAmI" в формат one hot
one_hot_data = pd.get_dummies(data['whoAmI'])
print("\nDataFrame в формате one hot с использованием get_dummies:")
print(one_hot_data.head())

# Без использования get_dummies
one_hot_data = pd.concat([pd.Series(1, index=data.index, name='robot'), pd.Series(0, index=data.index, name='human')], axis=1)
print("\nDataFrame в формате one hot без использования get_dummies:")
print(one_hot_data.head())