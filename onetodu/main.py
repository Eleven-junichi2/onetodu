from kivy.app import App
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.config import Config

LabelBase.register("NotoSansCJKjp-DemiLight",
                   fn_regular="./fonts/NotoSansCJKjp-DemiLight.otf")

Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')


class ToDoListItem(BoxLayout):
    label = ObjectProperty(None)

    def __init__(self, label_text, **kwargs):
        super().__init__(**kwargs)
        self.label.text = label_text


class MainScreen(Screen):
    todo_list = ObjectProperty(None)
    new_todo_text_input = ObjectProperty(None)

    def add_todo(self, todo_text):
        if todo_text:
            self.todo_list.add_widget(ToDoListItem(label_text=todo_text))


class OnetoduScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MainScreen(name="main"))


class OnetoduApp(App):
    def build(self):
        self.title = "Onetodu"
        self.icon = "images/onetodu.png"
        return OnetoduScreenManager()


def main():
    OnetoduApp().run()


if __name__ == '__main__':
    main()
