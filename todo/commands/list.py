# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os
import sys
import json

from todo.commands.base import Command
from todo.utils.styles import Fore, Back, Style


class ListCommand(Command):
    def print_project_name(self, name):
        if not name:
            name = self.UNTITLED_NAME
        print(
            '{bold}{blue}{name:>14}{reset}'
            .format(
                name=name,
                blue=Fore.BLUE,
                bold=Style.BOLD,
                reset=Style.RESET_ALL,
            )
        )


    def print_todos(self, todos=[]):
        checked = lambda t: t.get('done')
        for todo in sorted(todos, key=checked):
            is_done = todo.get('done')
            status = ' ✓ ' if is_done else ' x '
            color = Fore.GREEN if is_done else Style.RESET_ALL
            background = Back.GREEN if is_done else Back.WHITE
            print(
                ' {black}{background}{status}{reset}  {color}{title}{reset}'
                .format(
                    status=status,
                    title=todo.get('title'),
                    color=color,
                    black=Fore.BLACK,
                    background=background,
                    reset=Style.RESET_ALL,
                )
            )


    def print_list(self, todos=[]):
        if not todos:
            print(
            '{green}Congrats! 🙂{reset}'
            .format(
                green=Fore.GREEN,
                reset=Style.RESET_ALL,
                )
            )
            print('There\'s nothing else to do. 🎉')
        else:
            self.print_todos(todos)

            no_items = len(todos)
            no_checked = len([t for t in todos if t.get('done') ])
            print(
                '{info}{no_items:>2} items: {no_checked} done, {no_unchecked} undone{reset}'
                .format(
                    no_items=no_items,
                    no_checked=no_checked,
                    no_unchecked=(no_items - no_checked),
                    info=Fore.INFO,
                    reset=Style.RESET_ALL,
                )
            )


    def run(self):
        try:
            with open(self.PROJECT_FILE, 'r') as project_file:
                data = json.load(project_file)
                name = data.get('name')
                todos = data.get('todos')
        except FileNotFoundError:
            self.ask_create_project()
            return
        except:
            print(
                '{fail}An error has occured while listing the todos{reset}'
                .format(
                    fail=Fore.FAIL,
                    reset=Style.RESET_ALL,
                )
            )
            sys.exit(1)

        self.print_project_name(name)
        self.print_list(todos)


List = ListCommand()
