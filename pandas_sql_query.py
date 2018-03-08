# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 16:41:50 2017

@author: James
"""

from sqlalchemy import create_engine

import pandas as pd

engine = create_engine('sqlite:///Chinook.sqlite')

df = pd.read_sql_query("SELECT * FROM Customer", engine)

#Hello world of SQL Queries
# Execute query and store records in DataFrame: df
df = pd.read_sql_query('SELECT * FROM Album', engine)

# Print head of DataFrame
print(df.head())

# Open engine in context manager
# Perform query and save results to DataFrame: df1
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Album")
    df1 = pd.DataFrame(rs.fetchall())
    df1.columns = rs.keys()

# Confirm that both methods yield the same result: does df = df1 ?
print(df.equals(df1))

#Complex query
# Execute query and store records in DataFrame: df
df = pd.read_sql_query('SELECT * FROM Employee WHERE EmployeeID >= 6 ORDER BY BirthDate', engine)

# Print head of DataFrame
print(df.head())

#inner join
# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute('SELECT Title, Name FROM Album INNER JOIN Artist on Album.ArtistID=Artist.ArtistID')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print head of DataFrame df
print(df.head())