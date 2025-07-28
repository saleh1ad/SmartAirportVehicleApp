
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class NotificationCenterScreen(Screen):
    def __init__(self, **kwargs):
        super(NotificationCenterScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='مركز الإشعارات'))
        layout.add_widget(Label(text='تنبيهات حية للأعطال والمهام'))
        self.add_widget(layout)
