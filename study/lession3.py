from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from math import *


class PlaylistWidget(ScrollView):
    def add_labels(self, *args):
        grid = self.ids.grid
        for i in range(148):
            a = Label()
            a.text = "Blah blah blah"
            a.font_size = 30
            a.size_hint_y = None
            a.size_hint_x = 1.0

            # set label height
            a.height = grid.row_default_height

            grid.add_widget(a)


kv = '''
PlaylistWidget:
    bar_width: 50
    size_hint: 1, .5
    scroll_type: ['bars']
    bar_inactive_color: 5, 20, 10, .5
    bar_color: 5, 10, 15, .8
    do_scroll_x: False
    do_scroll_y: True
    GridLayout:
        id: grid
        cols: 1
        row_default_height: '20dp'
        row_force_default: True
        size_hint_y: None
        height: 50
'''


class TestApp(App):
    def build(self):
        pl = Builder.load_string(kv)
        Clock.schedule_once(pl.add_labels)
        return pl


TestApp().run()
