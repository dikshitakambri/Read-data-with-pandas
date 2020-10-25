#reading data

import pandas as pd

filepath = "C:/AI/Intel-ML101-Class1/Intel-ML101_Class1/data/Iris_Data.csv"

data = pd.read_csv(filepath)

#print(data.iloc[:5])

#Create a new column that is a product of two data

data['sepal_area'] = data.sepal_length*data.sepal_width

#print(data.iloc[:5, 3:])

#lambada function

data['abbrev'] = data.species.apply(lambda x : x.replace('Iris-',''))

#print(data.iloc[:5, 3:])

small_data = pd.concat([data.iloc[:2],data.iloc[-3:]])
#print(small_data.iloc[:,3:])

group_size = data.groupby('species').size()
print(group_size)

print(data.mean())