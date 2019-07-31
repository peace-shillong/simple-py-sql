#Read and Display Employee Details from employee table
import mysql.connector as sqltor
mycon = sqltor.connect(host='localhost',
                             database='company',
                             user='root',
                             password='')
if mycon.is_connected():
   print('Successfully Connected')
      
sql_select_Query = "select * from employee"
   
cursor = mycon.cursor()
cursor.execute(sql_select_Query)
   
records = cursor.fetchall()
print("Total number of rows in employee is - ", cursor.rowcount)
   
print ("Printing each row's column values i.e.  employee record")

for row in records:
   print(row)
cursor.close()

    #closing database connection.
if(mycon .is_connected()):
   mycon.close()
   print("MySQL connection is closed")
