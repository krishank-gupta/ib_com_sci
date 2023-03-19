from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.datatables import MDDataTable
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

class tablepage(MDApp):
    def build(self):
        pass

class TableScreen(MDScreen):

    # class variable
    data_table = None

    def on_pre_enter(self, *args):
        # before the screen is created, this code runs
        self.data_table = MDDataTable(
            size_hint = (.8, .5),
            pos_hint = {"center_x": .5, "center_y": .5},
            use_pagination = False,
            check = True,
            column_data = [
                ("id", 40), 
                ("Sender ID", 30),
                ("Receiver ID", 33),
                ("Amount", 30),
                ("Hash", 200)
            ]
        )
        self.data_table.bind(on_row_press = self.row_press),
        self.data_table.bind(on_check_press = self.check_pressed),
        self.add_widget(self.data_table)
        self.update()

    def row_press(self, table, row):
        print("row was pressed", row.text)
        row.md_bg_color = "#ff0000"

    def check_pressed(self, table, current_row):
        print("A check mark was pressed", current_row)

    def save(self):
        print("trying to save new tx")

        # pseudocode
        # get input values from md text field
        # build hash
        # insert into ledger (sender_id, receiver_id, amount, hash) values ()
        # commit and save in database
        # run self.update method to update the table

    def delete_selected_row(self):
        checked_rows = self.data_table.get_row_checks()
        # print(checked_rows)

        for row in checked_rows:
            id = row[0]
            query = f"delete from ledger where id = {id}"
            db = database_worker("bitcoin_exchange.db")
            db.run_save(query)
        db.close()
        self.update()

    def update(self):
        db = database_worker("bitcoin_exchange.db")
        query = "select * from ledger"
        data = db.search(query)
        db.close()
        self.data_table.update_row_data(None, data)
        
tablepage().run()
