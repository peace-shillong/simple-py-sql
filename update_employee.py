#UPDATE WITH INPUT
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
try:
   conn = mysql.connector.connect(host='localhost',
                             database='company',
                             user='root',
                             password='')
   print ("Enter Employee ID")
   emp_id=input()
   cursor = conn.cursor()
   print ("Before updating record ")
   sql_select_query = """select * from employee where id = %d""" % (emp_id)
   cursor.execute(sql_select_query)
   record = cursor.fetchone()
   print (record)
   #Update single record now
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

   sql_update_query = """Update employee set name=%s, designation=%s, qualification=%s,dob=%s,address=%s,gender=%s  where id = %d""" %(name,des,qua,dob,addr,gen,emp_id)
   cursor.execute(sql_update_query)
   conn.commit()
   print ("Record Updated successfully ")
   print("After updating record ")
   cursor.execute(sql_select_query)
   record = cursor.fetchone()
   print(record)
except mysql.connector.Error as error :
    print("Failed to update record to database: {}".format(error))
finally:
    #closing database connection.
    if(conn.is_connected()):
        conn.close()
        print("connection is closed")
