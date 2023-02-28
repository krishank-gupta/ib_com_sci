from library import verification
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCardSwipe
from kivy.properties import StringProperty

class main(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"
        return 
    
    def remove_item(self, instance):
        instance.ids.content.text = "Removed"  # Change text to "Removed"
        
class Login(MDScreen):
    def try_login(self):
        username = self.ids.login_username.text
        password = self.ids.login_password.text

        if not username:
            self.ids.login_username.error = True

        elif not password:
            self.ids.login_password.error = True

        # else hash password

        # store in db

class Register(MDScreen):
    def register(self):

        email = self.ids.register_email.text
        username = self.ids.register_username.text
        first_pswd = self.ids.register_password.text
        second_pswd = self.ids.register_password_verify.text
        
        if not verification.email_verify(email):
            self.ids.register_email.error = True
        elif not verification.str_input_verify(username):
            self.ids.register_username.error = True
        elif not verification.pswds_verify(first_pswd, second_pswd):
            self.ids.register_password_verify.error = True
        else:
            print("registration success")
            self.parent.current = "Dashboard"

class Dashboard(MDScreen):
    pass

class SwipeToDeleteItem(MDCardSwipe):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    text = StringProperty()

class ViewFridge(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def populate_list(self):
        for i in range(20):
            self.ids.md_list.add_widget(
                SwipeToDeleteItem(text=f"One-line item {i}")
            )
    

class AddItems(MDScreen):
    pass

class ViewLog(MDScreen):
    pass

main().run()
