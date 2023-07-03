import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",  #host name
  user="root",       #username
  password="",		 #password 
  database="GlsUniversity1" # databases name
)


mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE Department(Department_id int(10) PRIMARY KEY  AUTO_INCREMENT, Department_name varchar(255))")
mycursor.execute("CREATE TABLE Course(Course_id int(10) PRIMARY KEY  AUTO_INCREMENT , Course_name varchar(255) , Course_year varchar(10) , Department_id int(10),FOREIGN  KEY(Department_id) REFERENCES Department(Department_id))")

