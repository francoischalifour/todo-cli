from __future__ import absolute_import

import os
import sys
import json

from todo.commands.base import Command
from todo.utils.styles import Fore, Style


class AddCommand(Command):
    def update_todos(self, todos=[]):
        """Creates a copy of the todo list with the new item"""
        new_todos = todos.copy()

        for item in self.get_titles_input():
            new_item = { "done": False, "title": item }
            new_todos.append(new_item)

        return new_todos


    def run(self):
        try:
            with open(self.PROJECT_FILE, 'r') as project_file:
                data = json.load(project_file)
        except FileNotFoundError:
            self.ask_create_project()
            self.run()
            return
        except:
            print(
                '{fail}An error has occured while adding todos.{reset}'
                .format(
                    fail=Fore.FAIL,
                    reset=Style.RESET_ALL,
                )
            )
            sys.exit(1)

        try: name = data['name']
        except: name = self.UNTITLED_NAME

        try: todos = data['todos']
        except: todos = []

        new_data = {
            'name': name,
            'todos': self.update_todos(todos)
        }

        self.update_project(new_data)


Add = AddCommand()
