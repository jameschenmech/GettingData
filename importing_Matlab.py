# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 11:54:44 2017

@author: James
"""
#Once again, this file contains gene expression 
#data from the Albeck Lab at UCDavis.
#You can find the data and some great documentation here.


import scipy.io
import matplotlib.pyplot as plt
import numpy as np


filename = 'data1.mat'

mat = scipy.io.loadmat(filename)

print(type(mat))

# Print the keys of the MATLAB dictionary
for key in mat.keys():
    print(key)
    
#alterantive
print(mat.keys())

# Print the type of the value corresponding to the key 'CYratioCyt'
print(mat['fret'])

# Print the shape of the value corresponding to the key 'CYratioCyt'
print((mat['fret']).shape)

# Subset the array and plot it
data = mat['fret'][25, 5:]
fig = plt.figure()
plt.plot(data)
plt.xlabel('time (min.)')
plt.ylabel('normalized fluorescence (measure of expression)')
plt.show()
