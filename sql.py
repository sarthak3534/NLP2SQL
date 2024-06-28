import sqlite3

connection=sqlite3.connect('STUDENTS.db')
cursor=connection.cursor()


table_info="""
create table STUDENTS(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT);
"""

cursor.execute(table_info)

cursor.execute('''insert into STUDENTS values('sarthak','Data Science','A',90)''');
cursor.execute('''insert into STUDENTS values('rushil','Data Science','A',99)''');
cursor.execute('''insert into STUDENTS values('manav','Data Science','A',95)''');
cursor.execute('''insert into STUDENTS values('malay','Data Science','A',80)''');
cursor.execute('''insert into STUDENTS values('jay','web','A',80)''');
cursor.execute('''insert into STUDENTS values('himanshu','web','A',100)''');
cursor.execute('''insert into STUDENTS values('savan','web','B',90)''');
cursor.execute('''insert into STUDENTS values('abhi','web','B',65)''');


data=cursor.execute('''SELECT *
FROM STUDENTS ''')


for x in data:
    print(x)

print("perfect done")

connection.commit()
connection.close()