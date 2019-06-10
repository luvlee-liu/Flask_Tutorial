import sqlite3  # import the single-file builtin lib sqlite3

connection = sqlite3.connect('data.db')  # connect the lib with my database 'data.db'

cursor = connection.cursor()  # create the cursor

create_table = "CREATE TABLE users (id int, username text, password text)"  # create the schema
cursor.execute(create_table)


insert_query = "INSERT INTO users VALUES(?, ?, ?)"  # insert a single row into the users table
user = (1, 'Jose', 'abc')
cursor.execute(insert_query, user)


users = [
    (2, 'Anna', 'bcd'),
    (3, 'Jone', 'efg')
]
cursor.executemany(insert_query, users)  # insert many rows


select_query = "SELECT * FROM users"
for user in cursor.execute(select_query):
    print(user)


connection.commit()


connection.close()
