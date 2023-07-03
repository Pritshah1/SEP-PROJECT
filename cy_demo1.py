# import the mysql data and connect
#install the xamp server for mysql  server 
import mysql.connector

#connect with Mysql server
mydb = mysql.connector.connect(
  host="localhost",  #host name
  user="root",       #username
  password="",		 #password 
)

#connect with mysql server and databases 
# mydb = mysql.connector.connect(
#   host="localhost",  #host name
#   user="root",       #username
#   password="",		 #password 
#   database="GlsUniversity" # databases name
# )

# store the databases connection
mycursor = mydb.cursor()

# Create Databases 
mycursor.execute("CREATE DATABASE GlsUniversity")

#Create table Department and Course
mycursor.execute("CREATE TABLE Department(Department_id int(10) PRIMARY KEY  AUTO_INCREMENT, Department_name varchar(255))")
mycursor.execute("CREATE TABLE Course(Course_id int(10) PRIMARY KEY  AUTO_INCREMENT , Course_name varchar(255) , Course_year varchar(10) , Department_id int(10),FOREIGN  KEY(Department_id) REFERENCES Department(Department_id))")


#insert data  Department 
mycursor.execute("INSERT INTO Department (Department_name) VALUES (('Administration'))")
mydb.commit()
print ( "1 record inserted, ID : ", mycursor.lastrowid )
print(mydb)


# Insert_data = mycursor.execute("INSERT INTO Department (Department_name) VALUES (%s)")
# Insert_value = [("Mangement"),("Law"),("Information Technlogy"),("Designing"),("Administration")]
# Mycursor.executemany(Insert_data, Insert_value)
# print(mydb)
# mydb.commit()

#insert data  Course
mycursor.execute("INSERT INTO Course (Course_name , Course_year , Department_id) VALUES ('BBA' , '3Year' ,'5')")
mydb.commit()

# inserted_data_course = mycursor.execute("INSERT INTO Course (Course_name , Course_year , Department_id) VALUES (%s ,%s ,%s))")
# Insert_value_course =[("Integreted MBA" , "5 Year" ,"1") , ("BCA", "3 Year" ,"3") ,("Designing" , "4 Year" ,"4" ) ,("LLB" , "3Year" , "2") , ("BBA" , "3Year" ,"5")]
# mycursor.executemany(inserted_data_course , Insert_value_course)
# print(mydb)
# mydb.commit()

#select the data  course and display data using line by line
mycursor.execute("SELECT * FROM Course")
myresult = mycursor.fetchall()
for x in myresult:
	print(x)
print(mycursor.rowcount, "was inserted.")

#select the data  Department
cursor.execute("SELECT * FROM Department")
myresult = mycursor.fetchall()
for x in myresult:
	print(x)
print(mycursor.rowcount, "was inserted.")