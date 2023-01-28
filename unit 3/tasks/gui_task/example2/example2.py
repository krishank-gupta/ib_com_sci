from kivymd.app import MDApp

class example2(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return

    def close(self):
        exit()

    
example2().run()