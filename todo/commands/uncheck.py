from __future__ import absolute_import

import os
import sys
import json

from todo.commands.check import CheckCommand
from todo.utils.styles import Fore, Style


class UncheckCommand(CheckCommand):
    def check_item(self, item):
        """Unchecks an item"""
        item_toggled = item.copy()
        item_toggled['done'] = False
        return item_toggled


Uncheck = UncheckCommand()
