from __future__ import absolute_import

import os
import sys
import json

from todo.commands.base import Command
from todo.utils.styles import Fore, Style


class CheckCommand(Command):
    def check_item(self, item):
        """Makes a checked copie of the item"""
        item_toggled = item.copy()
        item_toggled['done'] = True
        return item_toggled


    def update_todo_item(self, data):
        """Checks the items matching the user input"""
        new_data = data.copy()
        item_titles = self.get_titles_input()

        if not 'todos' in new_data:
            print(
                '{warning}No todo idems{reset}'
                .format(
                    warning=Fore.WARNING,
                    reset=Style.RESET_ALL,
                )
            )
            sys.exit()
        else:
            todos = new_data['todos']
            items_matching = [ item for item in todos if item['title'] in item_titles ]
            if items_matching:
                for item_to_check in items_matching:
                    todos.remove(item_to_check)
                    todos.append(self.check_item(item_to_check))
            else:
                print(
                    '{fail}Unknown todo item{reset}'
                    .format(
                        fail=Fore.WARNING,
                        reset=Style.RESET_ALL,
                    )
                )
                sys.exit()

        return new_data


    def run(self):
        try:
            with open(self.PROJECT_FILE, 'r') as project_file:
                data = json.load(project_file)
        except FileNotFoundError:
            self.project_not_found()

        self.update_project(self.update_todo_item(data))


Check = CheckCommand()
