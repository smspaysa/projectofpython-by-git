import sqlite3
#connect to a database (creates a new one if it does)
conn=sqlite3.connect('mydatabase.db')
cursor=conn.cursor()

#define table structure
# cursor.execute('''
#        CREATE TABLE IF NOT EXISTS users(
#            id INTEGER PRIMARY KEY,
#            username TEXT NOT NULL,
#            age INTEGER,
#            email TEXT UNIQUE
#         )
#     ''')
# #commit the transaction
# conn.commit()


#insert record
# cursor.execute("INSERT INTO users (username,age,email) VALUES('Alice',30,'alice@example.com')")


#insert multiple records
# users=[
#     ('Bob',25,'bod@example.com'),
#     ('Charlie',35,'charlie@example.com')
# ]
# cursor.executemany("INSERT INTO users (username,age,email) VALUES(?,?,?)",users)


# #commit the transaction
# conn.commit()


#Retrive all records
# cursor.execute("SELECT * FROM users")
# rows=cursor.fetchall()
# for row in rows:
#     print(row)


#update records
# cursor.execute("UPDATE users SET age=31 WHERE username='Alice'")
# conn.commit()


#delete records
cursor.execute("DELETE FROM users WHERE username='Bob'")
conn.commit()


#close the cursor and connection
cursor.close()
conn.close()