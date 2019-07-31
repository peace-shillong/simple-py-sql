#UPDATE WITH INPUT
import mysql.connector as sqltor
mycon = sqltor.connect(host='localhost',
                             database='company',
                             user='root',
                             password='')

print ("Update Employee Details")
print ("Enter Employee ID")
emp_id=int(input())

cursor = mycon.cursor()

print ("Before updating record ")
sql_select_query = "select * from employee where emp_id =%s" %(emp_id,)
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
print ("Enter Employee DOB(DD/MM/YYYY)")
dob=input()
print ("Enter Employee Address")
addr=input()
print ("Enter Employee Gender(Male/Female)")
gen=input()

sql_update_query = """Update employee set name=%s, designation=%s, qualification=%s,dob=%s,address=%s,gender=%s where emp_id = %s""" 
cursor.execute(sql_update_query,(name,des,qua,dob,addr,gen,emp_id))
mycon.commit()
print ("Record Updated successfully ")

print("After updating record ")
cursor.execute(sql_select_query)
record = cursor.fetchone()
print(record)
    #closing database connection.
if(mycon.is_connected()):
   mycon.close()
   print("connection is closed")
