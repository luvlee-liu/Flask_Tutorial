import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# entries = [
#     (1, 'bob', 'asdf'),
# #     (2, 'jose', 'asdf'),
# #     (3, 'ana', 'asdf')
# ]
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

# insert_entries = "INSERT INTO users VALUES(?, ?, ?)"
# cursor.executemany(insert_entries, entries)
#
# select_query = "SELECT * FROM users"
# for user in cursor.execute(select_query):
#     print(user)

connection.commit()
connection.close()
