import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import csv
from kivy.uix.scrollview import ScrollView
from kivy.uix.carousel import Carousel
from kivy.effects.kinetic import KineticEffect
from kivy.base import runTouchApp


class ProfileWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


Build_LearnAB = Builder.load_file('lession4.kv')


class LearnScrollViewApp(App):
    def build(self):
        return Build_LearnAB


if __name__ == "__main__":
    LearnScrollViewApp().run()
