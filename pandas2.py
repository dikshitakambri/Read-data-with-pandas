#reading data

import pandas as pd

filepath = "Data/Iris_Data.csv"

data = pd.read_csv(filepath)

print(data.iloc[:5])

#Create a new column that is a product of two data

data['sepal_area'] = data.sepal_length*data.sepal_width

print(data.iloc[:5, 3:])

#lambada function

data['abbrev'] = data.species.apply(lambda x : x.replace('Iris-',''))

print(data.iloc[:5, 3:])

#concatenation

small_data = pd.concat([data.iloc[:2],data.iloc[-3:]])
print(small_data.iloc[:,3:])

#size of series

group_size = data.groupby('species').size()
print(group_size)

#mean median varience standard-deviation SEM quantile describe
print(data.mean())

print(data.petal_width.median())

print(data.petal_width.mode())

print(data.petal_width.std(),data.petal_width.var(),data.petal_width.sem())

print(data.quantile(0))

print(data.describe())

#sample from dataset

sample = (data.sample(n=5,replace=False,random_state=2))
print(sample.iloc[:,4:])