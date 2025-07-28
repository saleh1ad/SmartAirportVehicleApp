from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text='تسجيل الدخول / Login', font_size=24))
        self.username = TextInput(hint_text='اسم المستخدم / Username')
        self.password = TextInput(hint_text='كلمة المرور / Password', password=True)
        login_btn = Button(text='دخول / Login')
        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(login_btn)
        self.add_widget(layout)