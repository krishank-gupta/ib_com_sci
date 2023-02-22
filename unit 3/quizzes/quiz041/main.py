from kivymd.app import MDApp

class ttt(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.x = True
        self.x_list = []
        self.o_list = []
        self.winner = False

    def build(self):
        return

    def play(self, btn):
        
        current_btn = eval(f"self.root.ids.btn{btn}")
        winning_combos = [[1, 2, 3],[4, 5, 6],[7, 8, 9],[1, 4, 7],[2, 5, 8],[3, 6, 9],[1, 5, 9],[3, 5, 7]]
        current_btn.md_bg_color_disabled = '#F1FAEE'

        if self.x:
            current_btn.text = 'X'
            current_btn.md_bg_color_disabled = '#1D3557'
            current_btn.disabled_color = '#E63946'
            current_btn.font_size = '32pt'
            self.x_list.append(btn)
            self.root.ids.turn_msg.text = f"Player O's Turn"

            for i in winning_combos:
                if all(items in self.x_list for items in i):
                    self.winner = 'X'

        else:
            current_btn.text = 'O'
            current_btn.md_bg_color_disabled = '#E63946'
            current_btn.disabled_color = '#1D3557'
            current_btn.font_size = '32pt'
            self.o_list.append(btn)
            self.root.ids.turn_msg.text = f"Player X's Turn"

            for i in winning_combos:
                if all(items in self.o_list for items in i):
                    self.winner = 'O'


        if self.winner:
            if self.winner == 'O':
                self.root.ids.turn_msg.text = ('Player O Wins')
            else:
                self.root.ids.turn_msg.text = ('Player X Wins')
            
            for i in range(1,10,1):
                btn_test = eval(f"self.root.ids.btn{i}")
                btn_test.disabled = True

        if int(len(self.x_list)) + int(len(self.o_list)) == 9:
            self.root.ids.turn_msg.text = ("It's a Draw")

        current_btn.disabled = True
        self.x = not self.x

    def reset(self):
        self.x = True
        self.x_list = []
        self.o_list = []
        self.winner = False
        self.root.ids.turn_msg.text = f"Player X's Turn"
        
        for i in range(1,10,1):
            btn = eval(f"self.root.ids.btn{i}")
            btn.disabled = False
            btn.md_bg_color = '#A8DADC'
            btn.md_bg_color_disabled = '#F1FAEE'
            btn.text = ''

ttt().run()