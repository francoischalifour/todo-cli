from __future__ import absolute_import

import os
import sys
import json

from todo.commands.toggle import ToggleCommand
from todo.utils.styles import Fore, Style


class UncheckCommand(ToggleCommand):
    def check_by_item(self, item):
        """Returns an unchecked copy of the item"""
        item_toggled = item.copy()
        item_toggled['done'] = False
        return item_toggled


Uncheck = UncheckCommand()
