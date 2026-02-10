import sqlite3


# connect to sql 

connection = sqlite3.connect("STUDENT.db")


#3 creation of curosr

cursor = connection.cursor()

# create Table

table_info="""

create table STUDENT (NAME VARCAHR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT);



"""

cursor.execute(table_info)


## Inster Some records 

cursor.execute(''' Insert Into STUDENT values ('Gan','Data Science','A',90)''')
cursor.execute(''' Insert Into STUDENT values ('jan','Math','c',80)''')
cursor.execute(''' Insert Into STUDENT values ('Jack','Social','B',30)''')
cursor.execute(''' Insert Into STUDENT values ('Nada','Ai Ml','A',90)''')
cursor.execute(''' Insert Into STUDENT values ('Vish','Ml','A',60)''')


print("records are ")

data=cursor.execute(''' select * From STUDENT''')

for row in data:
    print(row)


connection.commit()
connection.close()
