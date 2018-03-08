# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 16:06:25 2017

@author: James
"""

from sqlalchemy import create_engine

engine = create_engine('sqlite:///Chinook.sqlite')

table_names = engine.table_names()

print(table_names)

import pandas as pd

con = engine.connect()

rs = con.execute("SELECT * FROM Artist")

df = pd.DataFrame(rs.fetchall()) #fetchall fetches all rows

df.columns = rs.keys()

con.close()

print(df.head())

#alternatively use construct method, advantage don't have to close connection

with engine.connect() as con:
    rs = con.execute("SELECT * FROM Invoice")
    df = pd.DataFrame(rs.fetchmany(size=5)) #fetch 5 install of all rows
    df.columns = rs.keys()

print(df.head())

#select all albums
# Perform query: rs
with engine.connect() as con:
    rs = con.execute('SELECT * FROM Album')
    # Save results of the query to DataFrame: df
    df = pd.DataFrame(rs.fetchall())


# Close connection
con.close()

# Print head of DataFrame df
print(df.head())


#Select specific columns
# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute('SELECT LastName, Title FROM Employee')
    df = pd.DataFrame(rs.fetchmany(size = 3))
    df.columns = rs.keys()

# Print the length of the DataFrame df
print(len(df))

# Print the head of the DataFrame df
print(df.head())

#filtering the database
# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute('SELECT * FROM Employee WHERE EmployeeID >= 6')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print the head of the DataFrame df
print(df.head())

#Use ordered by

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Open engine in context manager
with engine.connect() as con:
    rs = con.execute('SELECT * FROM Employee ORDER BY BirthDate ')
    df = pd.DataFrame(rs.fetchall())

    # Set the DataFrame's column names
    df.columns = rs.keys()

# Print head of DataFrame
print(df.head())

#filtering your inner join
# Execute query and store records in DataFrame: df
df = pd.read_sql_query('SELECT * FROM PlaylistTrack \
                       INNER JOIN Track on \
                       PlaylistTrack.TrackId = Track.TrackId \
                       WHERE Milliseconds < 250000', engine)

# Print head of DataFrame
print(df.head())
