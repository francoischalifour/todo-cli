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


    def handle_click(self, item_index, items):
        "Removes the item clicked"
        items.pop(item_index)
        return items


    def handle_search(self, todos, item):
        """Removes the item found"""
        todos.remove(item)


Remove = RemoveCommand()
