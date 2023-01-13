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
        if not isinstance(name, str):
            raise ValueError()
    
        return f"Holder's name set to {name}"

    def set_holder_email(self, email):
        if not email.count('@') == 1:
            raise ValueError()
        email_name, domain = email.split('@')
        if not domain.count('.') == 1:
            raise ValueError()

        return f"Holder's email set to {email}"

    def deposit(self, amount):
        self.balance += amount
        return f"New balance: {amount} USD"

    def get_balance(self):
        return self.balance