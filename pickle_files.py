# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 10:33:46 2017

@author: James
"""

import os
wd = os.getcwd()
print(os.listdir(wd))

import pickle

#putting  string into a new pickle file
a = ['test value', 'test_value_2', 'test value 3']

file_Name = "testfile.pkl"
fileObject = open(file_Name, 'wb')

pickle.dump(a, fileObject)

fileObject.close()

#Importing pickle file
# Open pickle file and load data: d
with open('testfile.pkl', 'rb') as file:
    d = pickle.load(file)

# Print d
print(d)

# Print datatype of d
print(type(d))
