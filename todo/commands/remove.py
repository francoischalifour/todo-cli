from __future__ import absolute_import

import os
import sys
import json

from todo.commands.toggle import ToggleCommand
from todo.utils.menu import show_options
from todo.utils.styles import Fore, Style


class RemoveCommand(ToggleCommand):
    def get_subtitle(self):
        """Returns the subtitle of the menu"""
        return 'Remove items'


    def handle_click(self, todos, item_index):
        """Returns the todo list without the todo of the given index"""
        todos_removed = todos.copy()
        todos_removed.pop(item_index)
        return todos_removed


    def handle_search(self, todos, item):
        """Returns the todo list without the given item"""
        todos_removed = todos.copy()
        todos_removed.remove(item)
        return todos_removed


Remove = RemoveCommand()
