from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from math import *
Builder.load_file("main.kv")

#    but_bak = ObjectProperty()
#    but_form = ObjectProperty()
#    but_calc = ObjectProperty()


class MainWindow(Screen):
    but_form = ObjectProperty()
    but_calc = ObjectProperty()

    def Ru_En(self, lang):
        if lang == "ru":
            self.but_form.text = "Формулы"
            self.but_calc.text = "Калькулятор"
            sm.get_screen('choice').ids.but_bak.text = "назад"

        elif lang == "en":
            self.but_form.text = "formulas"
            self.but_calc.text = "Calculator"
            sm.get_screen("choice").ids.but_bak.text = "back"


class CalcWindow(Screen):
    calc_lab = ObjectProperty()

    formula = '0'

    #    def Ru_En(self, lang):
    #        if lang == "ru":
    #            self.but_bak.text = "назад"
    #
    #        elif lang == "en":
    #            self.but_bak.text = "back"

    def add_number(self, instance):
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
        self.calc_lab.text = self.formula


class ChoiceWindow(Screen):
    pass


class InfoWindow(Screen):
    pass


# class Uprava(MainWindow, CalcWindow):


# class WindowManager(ScreenManager):
#    pass


# WindowManager().add_widget(MainWindow(name="main"))
# WindowManager().add_widget(CalcWindow(name="calc"))
# WindowManager().add_widget(ChoiceWindow(name="choice"))
# WindowManager().add_widget(InfoWindow(name="info"))


sm = ScreenManager()
sm.add_widget(MainWindow(name='main'))
sm.add_widget(CalcWindow(name='calc'))
sm.add_widget(ChoiceWindow(name='choice'))


class MyApp(App):
    #    but_form = ObjectProperty()
    #    but_calc = ObjectProperty()

    #    def Ru_En(self, lang):
    #        if lang == "ru":
    #            self.but_form.text = "Формулы"
    #            self.but_calc.text = "Калькулятор"
    #        elif lang == "en":
    #            self.but_form.text = "formulas"
    #            self.but_calc.text = "Calculator"

    def build(self):
        return sm


if __name__ == "__main__":
    MyApp().run()
