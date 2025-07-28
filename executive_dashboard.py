
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class ExecutiveDashboardScreen(Screen):
    def __init__(self, **kwargs):
        super(ExecutiveDashboardScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='لوحة القيادة التنفيذية'))
        layout.add_widget(Label(text='مؤشرات الأداء - المهام - المركبات - الإنذارات'))
        self.add_widget(layout)
