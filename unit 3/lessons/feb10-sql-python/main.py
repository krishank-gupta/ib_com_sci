import sqlite3

# class database_handler:

connection = sqlite3.connect("logindatabase.db")

# get the cursor to the database
cursor = connection.cursor()

# step 3
query = """CREATE TABLE users(
    id integer primary key,
    email text not null unique,
    password text not null,
    username text not null
);"""

cursor.execute(query)

# step 4 save changes

connection.commit()

# close database connection
connection.close()



# import sqlite3

# connection = sqlite3.connect("logindatabase.db")

# # get the cursor to the database
# cursor = connection.cursor()

# # step 3
# query = """CREATE TABLE users(
#     id integer primary key,
#     email text not null unique,
#     password text not null,
#     username text not null
# );"""

# cursor.execute(query)

# # step 4 save changes

# connection.commit()

# # close database connection
# connection.close()