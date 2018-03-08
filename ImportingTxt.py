# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 15:09:37 2017

@author: James
"""
import numpy as np
import pandas as pd

filename = 'seaslug.txt'

file = open(filename, mode='r') #mode ='w' to write

text = file.read()

file.close()

#print(text)

with open(filename, 'r') as file: #don't have to close a context
    print(file.read())
#with a context manager
#best practice to use with construct
    
# Read & print the first 3 lines
with open(filename) as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())
    
data = np.loadtxt(filename, skiprows=1, delimiter='\t')  #skip the header
#additional parameter, if only want 1 and 3rd cols, use usecols=[0,2]
#import alls as strings, dtype=str

df = pd.read_table(filename, header=0, sep='\t') #keep the header with pandas

# Assign filename to variable: file
file = 'mnist_kaggle_some_rows.csv'

# Load file as array: digits
digits = np.loadtxt(file, delimiter=',')

# Print datatype of digits
print(type(digits))

# Select and reshape a row
im = digits[21, 1:]
im_sq = np.reshape(im, (28, 28))

import matplotlib.pyplot as plt

# Plot reshaped data (matplotlib.pyplot already loaded as plt)
plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
plt.show()


#importing different datatypes
# Assign filename: file
file = 'seaslug.txt'

# Import file: data
data = np.loadtxt(file, delimiter='\t', dtype=str)

# Print the first element of data
print(data[0])

# Import data as floats and skip the first row: data_float
data_float = np.loadtxt(file, delimiter='\t', dtype=float, skiprows=1)

# Print the 10th element of data_float
print(data_float[9])

# Plot a scatterplot of the data
plt.scatter(data_float[:, 0], data_float[:, 1])
plt.xlabel('time (min.)')
plt.ylabel('percentage of larvae')
plt.show()

#imporitng mixed datatypes into a structured array
#access columns with index, rows with i=1,2,3,...
data = np.genfromtxt('titanic_sub.csv', delimiter=',', names=True, dtype=None)
print(data['Fare'])
print(data[0])

#working with mixed datatypes
# Assign the filename: file
file = 'titanic_sub.csv'

# Import file using np.recfromcsv: d
d = np.recfromcsv(file)

# Print out first three entries of d
print(d[:3])
