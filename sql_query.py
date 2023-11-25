import sqlite3
import pandas as pd

# import mysql.connector as sql

# conn = sql.connect(
#   host="localhost",
#   user="abid",
#   password="12345",
#   database="datacamp_python"
# )


# connecting to the database
connection = sqlite3.connect("db.sqlite3")

# # cursor
# crsr = connection.cursor()

# # close the connection
# connection.close()
 
cursor = connection.cursor()
cursor.execute("""SELECT *FROM Details""")
cursor.fetchall()
connection.close()




1. ###############################  Write a query to find the third-highest salary from the tables
#Answer = SELECT salary FROM emptable ORDER BY salary DESC LIMIT 2,1 

# LIMIT 1,1 = select one row after first row i.e 2 nd highest 
# LIMIT 3,1 = select one row after first row i.e 2 nd highest 
# LIMIT 4,1 = select one row after first row i.e 2 nd highest 


2.######################### 