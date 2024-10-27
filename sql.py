import sqlite3

## db create
connection=sqlite3.connect("student.db")

##cursor create
cursor=connection.cursor()


table_info = """
Create Table STUDENT(NAME VARCHAR (25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT)
"""

cursor.execute(table_info)

cursor.execute('''Insert Into STUDENT values('Krish','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Sudhanshu','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Darius','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Vikash','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Dipesh','DEVOPS','A',35)''')


print("The isnerted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)


## Commit your changes int he databse
connection.commit()
connection.close()