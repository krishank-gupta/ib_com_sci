from library import verification
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCardSwipe
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty

class main(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        return 
    
    def logout(self):
        self.root.current = "Login"

    def try_dashboard(self):
        print("try dashboard attempted")

    def goback(self):
        self.root.current = "Dashboard"
        
class Login(MDScreen):
    def try_login(self):
        username = self.ids.login_username.text
        password = self.ids.login_password.text

        if not verification.str_input_verify(username):
            self.ids.login_username.error = True

        elif not verification.str_input_verify(password):
            self.ids.login_password.error = True

        else: 
            self.parent.current = 'Dashboard'
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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    

class SwipeToDeleteItem(MDCardSwipe):
    text = StringProperty()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def remove_item(self, instance):
        print(instance.ids.content.text)
        instance.ids.content.text = "Removed"

    def edit_item(self, instance):
        print("edit screen", instance.ids.content.text)
    
class CustomTopAppBar(MDBoxLayout):
    titletext = StringProperty("")

class ViewFridge(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def populate_list(self):
 
        data = [1,2,3,4,5,6]
        for i in data:
            self.ids.md_list.add_widget(
                SwipeToDeleteItem(text=str(i))
            )


class AddItems(MDScreen):
    pass

class ViewLog(MDScreen):
    pass

main().run()
