from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string("""
<MenuScreen>:

    BoxLayout:
        orientation: "vertical"

        TextInput:
            id: word
            multiline: False

        Button:
            text: 'дальше'
            on_press: 
                root.pars(word.text)
                root.manager.current = 'settings'


<SettingsScreen>:

    BoxLayout:

        Label:
            id: label

        Button:
            text: "Назад"
            on_press: root.manager.current = 'menu'
        Button:
            text: "вперед"
            on_press: root.manager.current = 'any'

            
<AnyScreens>:
    BoxLayout:

        Label:
            id: label2

        Button:
            text: "Назад"
            on_press: root.manager.current = 'menu' 
""")


class MenuScreen(Screen):
    def pars(self, text):
        sm.get_screen('settings').ids.label.text = text
        sm.get_screen('any').ids.label2.text = text + "123"


class SettingsScreen(Screen):
    pass


class AnyScreens(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsScreen(name='settings'))
sm.add_widget(AnyScreens(name='any'))


class TestApp(App):
    def build(self):
        return sm


if __name__ == '__main__':
    TestApp().run()
