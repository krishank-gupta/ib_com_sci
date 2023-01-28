from kivymd.app import MDApp

class example3(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return

    def change_author(self, name):
        self.root.ids.title.text = f"Author {name}"
    
example3().run()