from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen


class MainWindow(Screen):
    pass


class CalcWindow(Screen):
    pass


class ChoiceWindow(Screen):
    pass


class InfoWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("main.kv")


class MyApp(App, CalcWindow):
    def build(self):
        return kv

    def __init__(self):
        super().__init__()
        self.formula = "0"

    def add_number(self, instance):
        if self.formula == "0":
            self.formula = ""

        self.formula += str(instance)
        self.update_label()

    def add_operation(self, instance):
        if str(instance).lower() == 'x':
            self.formula += '*'
        else:
            self.formula += str(instance)
        self.update_label()

    def update_label(self):
        CalcWindow().Label.text = self.formula


if __name__ == "__main__":
    MyApp().run()
