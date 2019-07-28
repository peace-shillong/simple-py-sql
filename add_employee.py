import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
try:
   mycon = mysql.connector.connect(host='localhost',
                                 database='company',
                                 user='root',
                                 password='')
                              
        # Take INPUT
   print ("Add New Employee ")
   print ("Enter Employee Name")
   name=input()
   print ("Enter Employee Designation")
   des=input()
   print ("Enter Employee Qualification")
   qua=input()
   print ("Enter Employee DOB")
   dob=input()
   print ("Enter Employee Address")
   addr=input()
   print ("Enter Employee Gender(Male/Female)")
   gen=input()
       
   sql_insert_query = """ INSERT INTO employee(name, designation, qualification, dob, address, gender) VALUES (%s, %s, %s, %s, %s, %s)"""  #%(name,des,qua,dob,addr,gen)
   cursor = mycon.cursor()
   result  = cursor.execute(sql_insert_query,(name,des,qua,dob,addr,gen)) #execute with params
   mycon.commit()
   print ("Record inserted successfully into employee table")
except mysql.mycon.Error as error :
   mycon.rollback() #rollback if any exception occured
   print("Failed inserting record into employee table {}".format(error))
finally:
        #closing database connection.
   if(mycon.is_connected()):
      cursor.close()
   mycon.close()
   print("MySQL connection is closed")
