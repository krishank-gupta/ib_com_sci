from library import verification
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCardSwipe
from kivymd.uix.button import MDFillRoundFlatIconButton, MDRectangleFlatIconButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.snackbar import BaseSnackbar
from kivy.core.window import Window
from kivymd.uix.behaviors import HoverBehavior
from kivymd.theming import ThemableBehavior
from kivy.properties import StringProperty, NumericProperty


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
            snackbar = CustomSnackbar(
                text="Log in Sucessful!",
                snackbar_x="10dp",
                snackbar_y="10dp",
                icon="information",
                bg_color=(66/254, 186/254, 150/254, 1),
            )
            snackbar.size_hint_x = (
                Window.width - (snackbar.snackbar_x * 2)
            ) / Window.width
            snackbar.open()
        
            self.parent.current = 'Dashboard'

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

class CustomSnackbar(BaseSnackbar):
    text = StringProperty(None)
    icon = StringProperty(None)
    font_size = NumericProperty("15sp")


# Custom Footer Class
class CustomTopAppBar(MDBoxLayout):
    titletext = StringProperty("")    

# Click to swipe Class
class SwipeToDeleteItem(MDCardSwipe):
    text = StringProperty()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def remove_item(self, instance):
        print(instance.ids.content.text)
        instance.ids.content.text = "Removed"

    def edit_item(self, instance):
        print("edit screen", instance.ids.content.text)

# Custom Hover Button main
class HoverButton(MDFillRoundFlatIconButton, ThemableBehavior, HoverBehavior):
    def on_enter(self, *args):
        self.md_bg_color = self.theme_cls.primary_dark

    def on_leave(self, *args):
        self.md_bg_color = self.theme_cls.primary_color

# Custom Hover Button Flat
class RectangleHoverButton(MDRectangleFlatIconButton, ThemableBehavior, HoverBehavior):
    def on_enter(self, *args):
        self.text_color = self.theme_cls.primary_dark
        self.icon_color = self.theme_cls.primary_dark

    def on_leave(self, *args):
        self.text_color = self.theme_cls.primary_color
        self.icon_color = self.theme_cls.primary_color



main().run()
