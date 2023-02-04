from kivymd.app import MDApp

class quiz38(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.counter = 0

    def build(self):
        return

    def click(self):
        self.counter += 1
        self.root.ids.counter_label.text = str(self.counter)

quiz38().run()


