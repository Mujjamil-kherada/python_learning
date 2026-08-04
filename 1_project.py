import sqlite3

creat=sqlite3.connect('student_id.db')
c=creat.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS STUDENT
            (ID INTEGER PRIMARY KEY,NAME TEXT,MARKS INTEGER)''')
c.execute("INSERT INTO student(name,marks) VALUES ('kasib','95')")
c.execute("INSERT INTO student(name,marks) VALUES ('muktar','65')")
c.execute("INSERT INTO student(name,marks) VALUES ('used','45')")
c.execute("INSERT INTO student(name,marks) VALUES ('rehan','35')")
c.execute("INSERT INTO student(name,marks) VALUES ('noman','85')")
c.execute("SELECT * FROM student")
rows = c.fetchall()
for row in rows:
    print(row)
creat.commit()
creat.close()

          