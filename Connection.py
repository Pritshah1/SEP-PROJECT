import mysql.connector

#connect with Mysql server
mydb = mysql.connector.connect(
  host="localhost",  #host name
  user="root",       #username
  password="",		 #password 
)

print(mydb)
