from kivymd.app import MDApp

class layout_demo(MDApp):
    # kwargs is a general term when we dont know the inputs
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.count = 0

    def build(self):
        return

    def change(self, name):
        
        if 'up' in name:
            self.count += 1
        else:
            self.count -= 1

        self.root.ids.counter_label.text = f"x={self.count}"

    def set_counter(self):
        inp_text = self.root.ids.user_start_x.text

        if not inp_text.isdigit():
            self.root.ids.counter_label.text = f"not int"
       
        else:
            self.count += int(inp_text) 
            self.root.ids.counter_label.text = f"x={self.count}"
        
        

layout_demo().run()

