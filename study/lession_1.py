# screen manager
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
# from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class Container(BoxLayout):
    pass


class FirstScreen(Screen):
    pass


class SecondScreen(Screen):
    pass


class WindowManager(ScreenManager):
    pass


# kv = Builder.load_file("lession_1.kv")


class MyApp(App):
    def build(self):
        return Container()


if __name__ == "__main__":
    MyApp().run()
