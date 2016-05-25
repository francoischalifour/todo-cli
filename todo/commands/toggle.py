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


    def check_by_item(self, item):
        """Returns a toggled copy of the item"""
        item_toggled = item.copy()
        status = item['done']
        item_toggled['done'] = not status
        return item_toggled


    def handle_click(self, todos, item_index):
        """Returns a copy of the todos with the toggled item clicked
        Function called when the user select the item in the interactive menu"""
        todos_toggled = todos.copy()
        item_to_toggle = todos[item_index]
        todos_toggled[item_index] = self.check_by_item(item_to_toggle)
        return todos_toggled


    def handle_search(self, todos, item):
        """Returns a copy of the todos with the toggled item found
        Function called when the item title has been typed in the command line"""
        todos_toggled = todos.copy()
        item_index = todos_toggled.index(item)
        item_to_toggle = todos_toggled[item_index]
        todos_toggled[item_index] = self.check_by_item(item_to_toggle)
        return todos_toggled


    def open_list(self, data, name):
        """Opens the interactive menu to toggle the items"""
        if len(data['todos']) == 0:
            raise KeyError

        try:
            return show_options(
                name,
                self.get_subtitle(),
                data['todos'],
                self.handle_click
            )
        except KeyboardInterrupt:
            self.cancel_command()


    def update_todos(self, data):
        """Returns the new todo list with the toggled items typed by the user
        Function called when the user types the items' names"""
        new_data = data.copy()
        items_titles = self.get_titles_input()
        options_all = ['-a', '--all']
        todos = new_data['todos']

        if items_titles[0].lower() in options_all:
            for item in todos:
                todos = self.handle_search(todos, item)
        else:
            items_matching = [ item for item in todos if item['title'] in items_titles ]
            if items_matching:
                for item_found in items_matching:
                    todos = self.handle_search(todos, item_found)

            titles_matching = [ item['title'] for item in items_matching ]
            items_not_found = [ item for item in items_titles if item not in titles_matching ]
            if items_not_found:
                print(
                    '{info}Unknown {items_print}: {items}{reset}'
                    .format(
                        info=Fore.INFO,
                        reset=Style.RESET_ALL,
                        items_print=('items' if len(items_not_found) > 1 else 'item'),
                        items=', '.join(items_not_found),
                    )
                )

            if not items_matching:
                sys.exit()

        return todos


    def run(self):
        try:
            with open(self.PROJECT_FILE, 'r') as project_file:
                data = json.load(project_file)
        except FileNotFoundError:
            self.project_not_found()
        except KeyError:
            print(
                '{fail}An error has occured while toggling the todos.{reset}'
                .format(
                    fail=Fore.FAIL,
                    reset=Style.RESET_ALL,
                )
            )
            sys.exit(1)

        try: name = data['name']
        except: name = self.UNTITLED_NAME

        try:
            if self.get_command_attributes():
                new_todos = self.update_todos(data)
            else:
                new_todos = self.open_list(data, name)
        except KeyError:
            print(
                '{warning}No items in the project.{reset}'
                .format(
                    warning=Fore.WARNING,
                    reset=Style.RESET_ALL,
                )
            )
            sys.exit()

        new_data = {
            'name': name,
            'todos': new_todos
        }

        self.update_project(new_data)


Toggle = ToggleCommand()
