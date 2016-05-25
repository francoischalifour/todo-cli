# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os
import sys
import json

from todo.commands.base import Command
from todo.utils.compatibility import safe_print
from todo.utils.styles import Fore, Back, Style


class ListCommand(Command):
    def print_project_name(self, name):
        """Prints the name of the project"""
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
        """Print all the todos"""
        checked = lambda t: t['done']
        for todo in sorted(todos, key=checked):
            is_done = todo['done']
            status = ' ✓ ' if is_done else ' x '
            color = Fore.GREEN if is_done else Style.RESET_ALL
            background = Back.GREEN if is_done else Back.WHITE
            safe_print(
                ' {black}{background}{status}{reset}  {color}{title}{reset}'
                .format(
                    status=status,
                    title=todo['title'],
                    color=color,
                    black=Fore.BLACK,
                    background=background,
                    reset=Style.RESET_ALL,
                )
            )


    def print_list(self, todos=[]):
        """Prints the entire todo list with information"""
        if not todos:
            safe_print(
                '{green}Congrats! 🙂{reset}'
                .format(
                    green=Fore.GREEN,
                    reset=Style.RESET_ALL,
                )
            )
            safe_print('There\'s nothing else to do. 🎉')
        else:
            self.print_todos(todos)

            no_items = len(todos)
            no_checked = len([t for t in todos if t['done'] ])
            print(
                '{info}{no_items:>2} items: {no_checked} completed, {no_unchecked} left{reset}'
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
        except FileNotFoundError:
            self.ask_create_project()
            return
        except:
            print(
                '{fail}An error has occured while listing the todos.{reset}'
                .format(
                    fail=Fore.FAIL,
                    reset=Style.RESET_ALL,
                )
            )
            sys.exit(1)

        try: name = data['name']
        except: name = self.UNTITLED_NAME

        try: todos = data['todos']
        except: todos = []

        self.print_project_name(name)
        self.print_list(todos)


List = ListCommand()
