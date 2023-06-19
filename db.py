import mysql.connector
#establishing the connection
conn = mysql.connector.connect(user='root', password='password', host='127.0.0.1')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Doping database MYDATABASE if already exists.
cursor.execute("DROP database IF EXISTS network")

#Preparing query to create a database
sql = "CREATE database network";

#Creating a database
cursor.execute(sql)

#Closing the connection
conn.close()

#table
conn = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='network')

#Dropping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS domain")

#Creating table as per requirement
sql ='''CREATE TABLE domain(
   id INT AUTO_INCREMENT,
   domain varchar(300),
   source varchar(30),
   waf varchar(100),
   link varchar(200),
   exploit varchar(200),
   shellcode varchar(200),
   PRIMARY KEY (id)
)'''
cursor.execute(sql)
#Closing the connection
conn.close()