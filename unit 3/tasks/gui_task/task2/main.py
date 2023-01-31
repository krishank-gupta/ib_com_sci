from kivymd.app import MDApp
from kivy.uix.label import Label

class task2(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return 

    def test(self):

        bits = self.root.ids.user_input.text
        
        if not bits.isdigit():
            self.root.ids.center_msg.text= f"Please enter an integer"
         
        else:
            outputs = [round(int(bits) / 8, 2)]
            suffixs = [
                "bytes",
                "KB",
                "MB",
                "GB",
                "TB",
                "PB",
                "EB",
            ]
            
            self.root.ids.center_msg.text = f"{bits} bits is {outputs[0]} bytes and..."

            for i in range(1, 7, 1):
                outputs.append( round(outputs[i-1] / 1024, 2))

                label = Label(
                    text = f"{ outputs[i]} { suffixs[i]}",
                    color=[0, 0, 0, 1],
                    bold=True
                )
                
                self.root.ids.container.add_widget(label)
   
task2().run()