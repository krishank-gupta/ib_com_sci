class Account:
    def __init__(self):
        self.balance = 0
        self.holder_name = ""
        self.holder_email = ""
        self.number = []

    def get_account_no(self):
        self.number = '000-00000-0'
        return self.number
    
    def set_holder_name(self, name):
        self.holder_name = name
        return self.holder_name

    def set_holder_email(self, email):
        self.holder_email = email
        return self.holder_email

    def get_balance(self):
        return self.balance


paula = Account()
print(paula.set_holder_name("Paula"))



