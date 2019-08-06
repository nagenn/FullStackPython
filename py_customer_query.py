
import mysql.connector
 
db = mysql.connector.connect(host="localhost",  # your host 
                     user="root",       # username
                     passwd="password",     # password
                     db="customers")   # name of the database
 
# Create a Cursor object to execute queries.
cur = db.cursor()
 
# Select data from table using SQL query.
cur.execute("SELECT * FROM customer_master")
 
# print the first and second columns      
for row in cur.fetchall() :
    print row[0], " ", row[1]
