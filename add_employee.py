import mysql.connector
    from mysql.connector import Error
    from mysql.connector import errorcode
    try:
       connection = mysql.connector.connect(host='localhost',
                                 database='company',
                                 user='root',
                                 password='')
                              
        /* Take INPUT*/
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
       
       sql_insert_query = """ INSERT INTO `employee`
                              (`name`, `designation`, `qualification`,`dob`,`address`,`gender`) VALUES (name,des,qua,dob, addr,gen)"""
       cursor = connection.cursor()
       result  = cursor.execute(sql_insert_query)
       connection.commit()
       print ("Record inserted successfully into employee table")
    except mysql.connector.Error as error :
        connection.rollback() #rollback if any exception occured
        print("Failed inserting record into employee table {}".format(error))
    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
