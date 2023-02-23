from passlib.context import CryptContext
import sqlite3


colors = {
    'green': '\033[92m',
    'red': '\033[91m',
    'end': '\033[0m'
}

pwd_config = CryptContext(schemes=["pbkdf2_sha256"],
                          default="pbkdf2_sha256",
                          pbkdf2_sha256__default_rounds=30000
                          )


def encrypt_password(user_password):
    return pwd_config.hash(user_password)

def check_password(hashed_password, user_password):
    return pwd_config.verify(user_password, hashed_password)

class database_handler:
    def __init__(self,dbname):
        self.connection = sqlite3.connect(dbname)
        self.cursor = self.connection.cursor()

    def run_query(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.connection.close()

db = database_handler("bitcoin_exchange.db")

db.run_query("select * from ledger")

data = (db.cursor.fetchall())

for i in data:
    hash = f"id {i[0]},sender_id {i[1]},receiver_id {i[2]},amount {i[3]}"
    if check_password(i[4], hash):
        print(f"{colors['green']} Tx(id={i[0]})Signature matches {colors['end']}")
    else:
        print(f"{colors['red']} Tx(id={i[0]})Error signature {colors['end']}")

db.close()