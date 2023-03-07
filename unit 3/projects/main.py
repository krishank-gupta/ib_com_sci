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
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.pickers import MDDatePicker
from kivy.properties import StringProperty, NumericProperty

class main(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "LightBlue"
        self.theme_cls.primary_hue = "300"  # "500"

        return 
    
    def logout(self):
        self.root.current = "Login"

    def goback(self):
        if self.root.current == "Dashboard":
            self.root.current = "Login"
        else:
            self.root.current = "Dashboard"
        

class Login(MDScreen):
    def try_login(self):
        username = self.ids.login_username.text
        password_field = self.ids.login_password
        password = password_field.ids.text_field.text

        if not verification.str_input_verify(username):
            self.ids.login_username.error = True

        elif not verification.str_input_verify(password):
            password_field.ids.text_field.error = True

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
        
        password_field = self.ids.register_password
        password_field_verify = self.ids.register_password_verify

        first_pswd = password_field.ids.text_field.text
        second_pswd = password_field_verify.ids.text_field.text
        
        if not verification.email_verify(email):
            self.ids.register_email.error = True
        elif not verification.str_input_verify(username):
            self.ids.register_username.error = True
        elif not verification.pswds_verify(first_pswd, second_pswd):
            password_field_verify.ids.text_field.error = True
        else:
            print("registration success")
            self.parent.current = "Dashboard"

class Dashboard(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_enter(self, *args):
        # return super().on_enter(*args)
        snackbar = CustomSnackbar(
                text="Warning!",
                snackbar_x="10dp",
                snackbar_y="10dp",
                icon="information",
                bg_color=(66/254, 186/254, 150/254, 1),
            )
        snackbar.size_hint_x = (
            Window.width - (snackbar.snackbar_x * 2)
        ) / Window.width
        snackbar.open()

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
    def on_save(self, instance, value, date_range):
        print(instance, value, date_range)
        self.ids.item_date.text=str(value)
        instance.dismiss(Force=True)

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(
            on_save=self.on_save, 
            on_cancel=self.on_cancel)
        date_dialog.open()
        self.ids.item_date.focus = False
        date_dialog.focus = True

    def on_cancel(self, instance, value):
        print("cancelled")
        instance.dismiss()

   

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

class ClickableTextFieldRound(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()
    helper_text = StringProperty()

    def tryingg(self):
        self.ids.eye_btns.theme_text_color = "Custom"
        app = MDApp.get_running_app()
        self.ids.eye_btns.text_color = app.theme_cls.primary_color

    def unfocus(self):
        self.ids.eye_btns.theme_text_color = "Custom"
        self.ids.eye_btns.text_color = "#ffffff"
main().run()
