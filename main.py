from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.login_screen import LoginScreen

class SmartAirportVehicleApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        return sm

if __name__ == "__main__":
    SmartAirportVehicleApp().run()
