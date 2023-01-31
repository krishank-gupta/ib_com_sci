from kivymd.app import MDApp

class main(MDApp):
    def build(self):
        return

    def hello_world(self):
        print("Hello from the console")
        self.root.ids.label.text = "Button Clicked"

main().run()