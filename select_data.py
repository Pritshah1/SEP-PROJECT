import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",  #host name
  user="root",       #username
  password="",		 #password 
  database="GlsUniversity1" # databases name
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Course")
myresult = mycursor.fetchall()
for x in myresult:
	print(x)
print(mycursor.rowcount, "was inserted.")

#select the data  Department



mycursor.execute("SELECT * FROM Department")
myresult = mycursor.fetchall()
for x in myresult:
	print(x)
print(mycursor.rowcount, "was inserted.")