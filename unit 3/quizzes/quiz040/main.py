from kivymd.app import MDApp

class quiz040(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dark = False

    def build(self):
        return

    def toggle(self):
        print(self.dark)
        if self.dark == True:
            self.dark = False
        else:
            self.dark = True
        print(self.dark)
        
        if self.dark:
            self.root.ids.scre.md_bg_color = "#000000"
            self.root.ids.text.color = "#ffffff"
            self.root.ids.btn.text = "Light Mode"

        else:
            self.root.ids.scre.md_bg_color = "#ffffff"
            self.root.ids.text.color = "#000000"
            self.root.ids.btn.text = "Dark Mode"

quiz040().run()


