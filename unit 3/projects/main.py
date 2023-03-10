from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivy.properties import StringProperty, NumericProperty
from kivymd.uix.card import MDCardSwipe
from kivymd.uix.button import MDFillRoundFlatIconButton, MDRectangleFlatIconButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.snackbar import BaseSnackbar
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.behaviors import HoverBehavior
from kivymd.theming import ThemableBehavior
from kivymd.uix.relativelayout import MDRelativeLayout

# Library Imports
from library import verification, general

# DB Imports
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String, Boolean, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select

Base = declarative_base()

# Database Tables Creation
class users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(250), unique=True, nullable=False)
    username = Column(String(250), unique=True, nullable=False)
    password = Column(String(300))
    active = Column(Boolean(), default=False)

    def __repr__(self) -> str:
        return f"""id: {self.id},email: {self.email},username: {self.username},password: {self.password}, active: {self.active}"""

class items(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    category = Column(String(250),nullable=False)
    expiry = Column(String(300), nullable=False)
    quantity = Column(Integer, nullable=False)
    owner = Column(String(300), nullable=False)

engine = create_engine('sqlite:///main.db')

Base.metadata.create_all(engine)
Base.metadata.bind = engine

session = sessionmaker(bind=engine)
database_session = session()

# make sure all users active state is false:
database_session.query(users).update({users.active: False})

# Simple Select all users query using SQL Alchemy
query = select(users)
res = database_session.execute(query).fetchall()

class main(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "LightBlue"
        self.theme_cls.primary_hue = "300"
        return 
    
    def logout(self):
        database_session.query(users).update({users.active: False})
        self.root.current = "Login"

    def goback(self):
        if self.root.current == "Dashboard":
            self.root.current = "Login"
        else:
            self.root.current = "Dashboard"

class Login(MDScreen):
    def on_pre_enter(self, *args):
        return super().on_pre_enter(*args)
    
    def try_login(self):

        # get user entered username and password
        username = self.ids.login_username.text
        password_field = self.ids.login_password
        password = password_field.ids.text_field.text
        
        query = database_session.query(users).filter(users.username == username)
        registered_users = database_session.execute(query).fetchall()
        
        db_pswd_query = database_session.query(users.password).filter(users.username == username)
        db_pswd = database_session.execute(db_pswd_query).fetchone()
        db_pswd = general.str_clean(db_pswd)

        if not verification.str_input_verify(username):
            self.ids.login_username.error = True

        elif not verification.str_input_verify(password):
            password_field.ids.text_field.error = True

        elif not registered_users:
            password_field.ids.text_field.error = True
            password_field.helper_text = "user not registered"

        elif not db_pswd == password:
            password_field.ids.text_field.error = True
            password_field.helper_text = "incorrect password"

        else: 
            database_session.query(users).filter(users.username == username).update({users.active: True})

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

            temp_user = users(email=email, username=username, password=first_pswd, active=True)
            
            database_session.add(temp_user)
            database_session.commit()

            self.parent.current = "Dashboard"

class Dashboard(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_enter(self, *args):

        query = select(users.username).where(users.active == True)
        res = database_session.execute(query).fetchall()
        name = (general.str_clean(res))

        self.ids.dashboard_title.text = f"Welcome {name}"


class ViewFridge(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def populate_list(self):
        print("hi")
        query = select(items)
        res = database_session.execute(query).fetchall()
        fridge = (general.str_clean(res))
        print(fridge)

        data = [1,2,3,4,5,6,7]
        for i in data:
            self.ids.md_list.add_widget(
                SwipeToDeleteItem(text=str(i))
            )

class AddItems(MDScreen):
    # def on_pre_enter(self):
    #     self.ids.item_name.text = ""
    #     self.ids.quantity.text = ""
    #     self.ids.item_date.text = ""

    def on_save(self, instance, value, date_range):
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
        instance.dismiss()

    def checkbox_click(self, checkbox, value, category):
        if value:  # if the check is true
            self.selected_category = category

    def register(self):
        # Get data from the add item screen form submission
        item_name = self.ids.item_name.text
        item_quantity = self.ids.quantity.text
        expiry = self.ids.item_date.text

        # get current logged in user name:
        query = select(users.username).where(users.active == True)
        res = database_session.execute(query).fetchall()
        current_user = (general.str_clean(res))
    
        temp_item = items(name=item_name, category=self.selected_category, expiry=expiry, quantity=item_quantity, owner=current_user)    
        database_session.add(temp_item)
        database_session.commit()

        snackbar = CustomSnackbar(
            text="Item added!",
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
