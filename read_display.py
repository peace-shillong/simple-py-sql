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
   print("Total number of rows in employee is - ", cursor.rowcount)
   print ("Printing each row's column values i.e.  employee record")
   for row in records:
       print("EMP Id = ", row[0], )
       print("Name = ", row[1])
       print("Designation  = ", row[2])
       print("Qualification  = ", row[3])
       print("DOB  = ", row[4])
       print("Address  = ", row[5])
       print("Gender  = ", row[6],"\n")      
   cursor.close()
   
except Error as e :
    print ("Error while connecting to MySQL", e)
finally:
    #closing database connection.
    if(mySQLconnection .is_connected()):
        connection.close()
        print("MySQL connection is closed")
