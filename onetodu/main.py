import json
import pathlib
import sys

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

DATA_DIR_NAME = "data"
DATA_FILE_NAME = "todo_list"
DATA_FILE_PATH = pathlib.Path(
    sys.argv[0]).parent / DATA_DIR_NAME / DATA_FILE_NAME


class TodoListManager:
    def __init__(self, manager_user):
        self.todo_list = []
        self.manager_user = manager_user

    def add_todo(self, todo_text: str):
        self.todo_list.append(todo_text)
        self.manager_user.update_list(self.todo_list)

    def remove_todo_by_text(self, todo_text: str):
        self.todo_list.remove(todo_text)
        self.manager_user.update_list(self.todo_list)

    def save_to_json(self, file_path):
        with open(file_path, "w") as file_obj:
            json.dump(self.todo_list, file_obj)

    def load_list_from_json(self, file_path):
        with open(file_path, "r") as file_obj:
            self.todo_list = json.load(file_obj)
        self.manager_user.update_list(self.todo_list)


class ToDoListItemWidget(BoxLayout):
    label = ObjectProperty(None)

    def __init__(self, label_text, **kwargs):
        super().__init__(**kwargs)
        self.label.text = label_text


class MainScreen(Screen):
    todo_list = ObjectProperty(None)
    new_todo_text_input = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def update_list(self, todo_list):
        self.todo_list.clear_widgets()
        for todo_text in todo_list:
            self.todo_list.add_widget(ToDoListItemWidget(label_text=todo_text))


class OnetoduScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MainScreen(name="main"))


class OnetoduApp(App):
    def build(self):
        self.title = "Onetodu"
        self.icon = "images/onetodu.png"
        self.screen_manager = OnetoduScreenManager()
        self.todo_list_manager = TodoListManager(
            self.screen_manager.get_screen("main"))
        return self.screen_manager

    def on_start(self):
        if DATA_FILE_PATH.parent.exists():
            self.todo_list_manager.load_list_from_json(
                str(DATA_FILE_PATH) + ".json")

    def on_stop(self):
        if not DATA_FILE_PATH.parent.exists():
            DATA_FILE_PATH.parent.mkdir()
        self.todo_list_manager.save_to_json(str(DATA_FILE_PATH) + ".json")


def main():
    OnetoduApp().run()


if __name__ == '__main__':
    main()
