
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class TaskAssignmentScreen(Screen):
    def __init__(self, **kwargs):
        super(TaskAssignmentScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='تخصيص المهام'))
        layout.add_widget(Label(text='تعيين المهام للمركبات حسب الموقع'))
        self.add_widget(layout)
