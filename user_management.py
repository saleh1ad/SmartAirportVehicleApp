
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class UserManagementScreen(Screen):
    def __init__(self, **kwargs):
        super(UserManagementScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='إدارة المستخدمين'))
        layout.add_widget(Label(text='إضافة وتعديل صلاحيات الفئات المختلفة'))
        self.add_widget(layout)
