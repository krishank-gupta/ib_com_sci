import sqlite3

class database_worker:
    def __init__(self, name):
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()

    def search(self, query):
        result = self.cursor.execute(query).fetchall()
        return result

    def run_save(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.connection.close()

# db = database_worker("bitcoin_exchange.db")
# query = "select * from ledger"
# data = db.search(query)
# db.close()
# self.data_table.update_row_data(None, data)