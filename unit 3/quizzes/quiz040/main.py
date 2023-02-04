from kivymd.app import MDApp

class quiz040(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dark = False

    def build(self):
        return

    def toggle(self):

        if self.dark == True:
            self.dark = False
        else:
            self.dark = True
        
        if self.dark:
            # dark mode
            self.root.ids.scre.md_bg_color = "#03001C"
            self.root.ids.text.color = "#B6EADA"
            self.root.ids.btn.text = "Light Mode"
            self.root.ids.btn.md_bg_color = "#B6EADA"
            self.root.ids.btn.text_color = '#03001C'

        else:
            # light mode
            self.root.ids.scre.md_bg_color = "#B6EADA"
            self.root.ids.text.color = "#03001C"
            self.root.ids.btn.text = "Dark Mode"
            self.root.ids.btn.md_bg_color = "#301E67"
            self.root.ids.btn.text_color = '#B6EADA'

quiz040().run()


