import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",  #host name
  user="root",       #username
  password="",		 #password 
  database="GlsUniversity1" # databases name
)

mycursor = mydb.cursor()

mycursor.execute("INSERT INTO Department (Department_name) VALUES ('Mangement')")
mycursor.execute("INSERT INTO Department (Department_name) VALUES ('Law')")
mycursor.execute("INSERT INTO Department (Department_name) VALUES ('Information Technlogy')")
mycursor.execute("INSERT INTO Department (Department_name) VALUES ('Designing')")
mycursor.execute("INSERT INTO Department (Department_name) VALUES ('Administration')")
mydb.commit()
print ( "1 record inserted, ID : ", mycursor.lastrowid )
print(mydb)


# Insert_data = mycursor.execute("INSERT INTO Department (Department_name) VALUES ('%s')")
# Insert_value = [("Mangement"),("Law"),("Information Technlogy"),("Designing"),("Administration")]
# mycursor.executemany(Insert_data, Insert_value)
# print(mydb)
# mydb.commit()

# insert data  Course
mycursor.execute("INSERT INTO Course (Course_name , Course_year , Department_id) VALUES ('Integreted MBA' , '5 Year' ,'1')")
mycursor.execute("INSERT INTO Course (Course_name , Course_year , Department_id) VALUES ('BCA', '3 Year' ,'3')")
mycursor.execute("INSERT INTO Course (Course_name , Course_year , Department_id) VALUES ('Designing' , '4 Year' ,'4' )")
mycursor.execute("INSERT INTO Course (Course_name , Course_year , Department_id) VALUES ('LLB' , '3Year' , '2')")
mycursor.execute("INSERT INTO Course (Course_name , Course_year , Department_id) VALUES ('BBA' , '3Year' ,'5')")
mydb.commit()
print ( "1 record inserted, ID : ", mycursor.lastrowid )
print(mydb)

# inserted_data_course = mycursor.execute("INSERT INTO Course (Course_name , Course_year , Department_id) VALUES ('%s' ,'%s' ,'%s')")
# Insert_value_course =[('Integreted MBA' , '5 Year' ,'1') , ('BCA', '3 Year' ,'3') ,('Designing' , '4 Year' ,'4' ) ,('LLB' , '3Year' , '2') , 
# 					('BBA' , '3Year' ,'5')]
# mycursor.executemany(inserted_data_course , Insert_value_course)
# print(mydb)
# mydb.commit()