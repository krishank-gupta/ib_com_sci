from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

class MysteryPageA(MDScreen):
    def message1(self):
        self.ids.label1.text = "This is mystery page A you pressed the button"

class MysteryPageB(MDScreen):
    def message2(self):
        self.ids.label2.text = "This is mystery page B you pressed the button"

class MysteryPageC(MDScreen):
    pass

class main(MDApp):
    def build(self):
        return

main().run()
