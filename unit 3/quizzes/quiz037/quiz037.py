class CompountInterest:
    def __init__(self, principal, rate, time) -> None:
        self.principal = principal
        self.rate = rate
        self.time = time
    
    def compound_interest_calculator(self):
        return int(self.principal) * (1+int(self.rate)) ** int(self.time)

    def __repr__(self) -> str:
        return "[CompoundInterest Class]"

class AccountingProgram:
    def __init__(self):
        self.data = CompountInterest(principal=0, rate=0, time=0)

    def __repr__(self) -> str:
        return f"[AccountingProgram Class] {self.data}"

    def set_principal(self, principal):
        self.data.principal = principal
    
    def set_rate(self, rate):
        self.data.rate = rate

    def set_time(self, time):
        self.data.time = time

    def calculate_interest(self):
        return self.data.compound_interest_calculator()
    

test = AccountingProgram()
test.set_principal(2)
test.set_rate(2)
test.set_time(4)
print(test.calculate_interest)

