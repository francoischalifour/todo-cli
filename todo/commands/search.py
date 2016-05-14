# -*- coding: UTF-8 -*-

from __future__ import absolute_import

import os
import sys
import json

from todo.commands.list import ListCommand
from todo.utils.styles import Fore, Back, Style


class SearchCommand(ListCommand):
    def get_matches(self, search, todos):
        """Returns items that match the query"""
        if not search:
            return None
        search_lower = search.lower()
        return [ todo for todo in todos if search_lower in todo.get('title').lower() ]


    def print_results(self, todos=[]):
        if not todos:
            print(
                '{info}No item found for "{query}"{reset}'
                .format(
                    query=self.get_command_attributes(),
                    info=Fore.INFO,
                    reset=Style.RESET_ALL,
                )
            )
        else:
            self.print_todos(todos)

            no_items = len(todos)
            print(
                '{info}{no_items:>2} {items} found{reset}'
                .format(
                    no_items=no_items,
                    items=('items' if no_items > 1 else 'item'),
                    info=Fore.INFO,
                    reset=Style.RESET_ALL,
                )
            )


    def run(self):
        try:
            with open(self.PROJECT_FILE, 'r') as project_file:
                data = json.load(project_file)
        except FileNotFoundError:
            self.project_not_found()
        except:
            print(
                '{fail}An error has occured while listing the todos{reset}'
                .format(
                    fail=Fore.FAIL,
                    reset=Style.RESET_ALL,
                )
            )
            sys.exit(1)

        name = data.get('name')
        todos = data.get('todos')
        todos_found = self.get_matches(self.get_command_attributes(), todos)

        self.print_results(todos_found)


Search = SearchCommand()
