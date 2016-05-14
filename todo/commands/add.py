from __future__ import absolute_import

import os
import sys
import json

from todo.commands.base import Command
from todo.utils.styles import Fore, Style


class AddCommand(Command):
    def update_todos(self, data):
        """Creates a copy of the todo list with the new item"""
        new_data = data.copy()

        if not 'todos' in new_data:
            new_data['todos'] = []

        for item in self.get_titles_input():
            new_item = {
                "done": False,
                "title": item
            }
            new_data['todos'].append(new_item)

        return new_data


    def run(self):
        try:
            with open(self.PROJECT_FILE, 'r') as project_file:
                data = json.load(project_file)
        except FileNotFoundError:
            self.ask_create_project()
            self.run()
            return

        self.update_project(self.update_todos(data))


Add = AddCommand()
