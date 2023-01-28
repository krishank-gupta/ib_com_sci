from kivymd.app import MDApp

class task1(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.amount = 0

    def build(self):
        return

    def converter_usd(self):
        amount = self.root.ids.user_input.text
        if not amount.isdigit():
            self.root.ids.output.text = f"Please enter an integer value"
        else:
            self.root.ids.output.text = f"{int(amount)} NPR is {round((int(amount) * 0.0077), 2)} USD"
    
    def converter_jpy(self):
        amount = self.root.ids.user_input.text

        if not amount.isdigit():
            self.root.ids.output.text = f"Please enter an integer value"
        else:
            self.root.ids.output.text = f"{int(amount)} NPR is {round((int(amount) * 0.994985),2)} JPY"

task1().run()

