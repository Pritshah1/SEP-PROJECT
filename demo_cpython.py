import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  #DATABASE = "GlsUniversity"
)



mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE GlsUniversity")
mycursor.execute("CREATE TABLE Department(Department_id int(10) PRIMARY KEY  AUTO_INCREMENT, Department_name varchar(255))")
mycursor.execute("CREATE TABLE Course(Course_id int(10) PRIMARY KEY  AUTO_INCREMENT , Course_name varchar(255) , Course_year varchar(10) ,
 FOREIGN  KEY(Department_id) REFERENCES Department(Department_id))")

Insert_data = mycursor.execute("INSERT INTO Department (Department_name) VALUES (%s)")
Insert_value = [("Mangement"),("Law"),("Information Technlogy"),("Designing"),("Administration")]
Mycursor.executemany(Insert_data, Insert_value)
print(mydb)
mydb.commit()


inserted_data_course = mycursor.execute("INSERT INTO Course (Course_name , Course_year , Department_id) VALUES (%s ,%s ,%s))")
Insert_value_course =[("Integreted MBA" , "5 Year" ,"1") , ("BCA", "3 Year" ,"3") ,("Designing" , "4 Year" ,"4" ) ,("LLB" , "3Year" , "2") , ("BBA" , "3Year" ,"5")]
mycursor.executemany(inserted_data_course , Insert_value_course)
print(mydb)


mycursor.execute("SELECT * FROM Course")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
print(mycursor.rowcount, "was inserted.")
