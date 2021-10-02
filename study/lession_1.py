# screen manager
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty


class FirstWindow(Screen):
    but = ObjectProperty()
    lab = ObjectProperty()

    def change_text(self):
        self.lab.text = self.but.text
        return self.lab.text


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


# class Container(FirstScreen, SecondScreen, WindowManager):
#     pass


kv = Builder.load_file("lession_1.kv")


class MyApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyApp().run()
