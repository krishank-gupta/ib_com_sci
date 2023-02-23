import sqlite3

haiku = """Code flows like a stream
Algorithms guide its way
In silence, it solves"""

class database_handler:
    def __init__(self,dbname):
        self.connection = sqlite3.connect(dbname)
        self.cursor = self.connection.cursor()

    def create_table(self):
        query = f"""CREATE TABLE words(
    id INTEGER PRIMARY KEY,
    word TEXT NOT NULL,
    length INTEGER NOT NULL);"""
        self.run_query(query)

    def run_query(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.connection.close()

db = database_handler("database.db")
db.create_table()

for word in haiku.split():
    query = f"""INSERT into words (word, length) VALUES('{word}', {len(word)})"""
    db.run_query(query)

db.run_query("select avg(length) from words")

print(db.cursor.fetchone())

db.close()