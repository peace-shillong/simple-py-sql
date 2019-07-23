//Read and Display Employee Details from employee table
import mysql.connector
from mysql.connector import Error
try:
   mySQLconnection = mysql.connector.connect(host='localhost',
                             database='company',
                             user='root',
                             password='')
   sql_select_Query = "select * from employee"
   cursor = mySQLconnection .cursor()
   cursor.execute(sql_select_Query)
   records = cursor.fetchall()
   print("Total number of rows in python_developers is - ", cursor.rowcount)
   print ("Printing each row's column values i.e.  employee record")
   for row in records:
       print("Id = ", row[0], )
       print("Name = ", row[1])
       print("JoiningDate  = ", row[2])
       print("Salary  = ", row[3], "\n")
   cursor.close()
   
except Error as e :
    print ("Error while connecting to MySQL", e)
finally:
    #closing database connection.
    if(mySQLconnection .is_connected()):
        connection.close()
        print("MySQL connection is closed")
