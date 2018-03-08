# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 23:23:25 2017

@author: James
"""

import pandas as pd

filename = 'titanic_sub.csv'

# Read the file into a DataFrame: df
df = pd.read_csv(filename)

# View the head of the DataFram
print(df.head())

df.head()

df_array = df.values #convert to numpy array

#importing partial files 
# Assign the filename: file
file = 'mnist_kaggle_some_rows.csv'

# Read the first 5 rows of the file into a DataFrame: data
data = pd.read_csv(file, header = None, nrows = 5)

# Build a numpy array from the DataFrame: data_array
data_array = data.values

# Print the datatype of data_array to the shell
print(type(data_array))