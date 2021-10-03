from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from math import *


class MainWindow(Screen):
    def Ru_En(self, lang):
        pass


class CalcWindow(Screen):
    calc_lab = ObjectProperty()
    formula = '0'

    def add_number(self, instance):
        print(instance)
        if self.formula == "0":
            self.formula = ""

        self.formula += instance
        self.update_label()

    def add_operation(self, instance):
        if str(instance).lower() == 'x':
            self.formula += '*'
        else:
            self.formula += str(instance)
        self.update_label()

    def calc_result(self, instance):

        self.calc_lab.text = str(eval(self.calc_lab.text))
        self.formula = "0"

    def clear_text(self):
        self.formula = '0'
        self.update_label()

#    def sqrt_text(self):
#        try:
#            self.calc_lab.text = int(self.calc_lab.text)
#
#        except:
#            self.calc_lab.text = str(eval('sqrt(self.calc_lab.text)'))
#        finally:
#            self.update_label()

    def update_label(self):
        print(self.formula)
        self.calc_lab.text = self.formula


class ChoiceWindow(Screen):
    pass


class InfoWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("main.kv")


class MyApp(App):

    def build(self):
        return kv


if __name__ == "__main__":
    MyApp().run()
