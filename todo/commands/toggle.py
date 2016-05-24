from __future__ import absolute_import

import os
import sys
import json

from todo.commands.base import Command
from todo.utils.menu import show_options
from todo.utils.styles import Fore, Style


class ToggleCommand(Command):
    def get_subtitle(self):
        """Returns the subtitle of the menu"""
        return 'Toggle items'


    def handle_click(self, todos, item_index):
        """Makes a toggled copy the item clicked"""
        todos_toggled = todos.copy()
        status = todos[item_index]['done']
        todos_toggled[item_index]['done'] = not status
        return todos_toggled


    def handle_search(self, todos, item):
        """Toggles the item found"""
        item_index = todos.index(item)
        todos[item_index] = self.check_by_item(item)


    def check_by_item(self, item):
        """Makes a toggled copy of the item"""
        item_toggled = item.copy()
        status = item_toggled['done']
        item_toggled['done'] = not status
        return item_toggled


    def open_list(self, data, name):
        """Open the menu to toggle items"""
        try:
            return show_options(
                name,
                self.get_subtitle(),
                data['todos'],
                self.handle_click
            )
        except KeyboardInterrupt:
            self.cancel_command()
        except KeyError:
            print(
                '{warning}No items in the project.{reset}'
                .format(
                    warning=Fore.WARNING,
                    reset=Style.RESET_ALL,
                )
            )
            sys.exit()


    def update_todos(self, data):
        new_data = data.copy()
        item_titles = self.get_titles_input()

        if not 'todos' in new_data:
            print(
                '{warning}No todo idems.{reset}'
                .format(
                    warning=Fore.WARNING,
                    reset=Style.RESET_ALL,
                )
            )
            sys.exit()

        todos = new_data['todos']
        items_matching = [ item for item in todos if item['title'] in item_titles ]
        if items_matching:
            for item_found in items_matching:
                self.handle_search(todos, item_found)
        else:
            print(
                '{warning}Unknown todo item.{reset}'
                .format(
                    warning=Fore.WARNING,
                    reset=Style.RESET_ALL,
                )
            )
            sys.exit()

        return todos


    def run(self):
        try:
            with open(self.PROJECT_FILE, 'r') as project_file:
                data = json.load(project_file)
                name = data['name']
        except FileNotFoundError:
            self.project_not_found()
        except:
            name = self.UNTITLED_NAME

        if self.get_command_attributes():
            new_todos = self.update_todos(data)
        else:
            new_todos = self.open_list(data, name)

        new_data = {
            'name': name,
            'todos': new_todos
        }

        self.update_project(new_data)


Toggle = ToggleCommand()
