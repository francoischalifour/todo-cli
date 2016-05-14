# -*- coding: utf-8 -*-

from __future__ import absolute_import

import sys
import json

from todo.utils.styles import Fore, Style


class Command:
    def __init__(self):
        self.usage = None
        self.description = None
        self.PROJECT_FILE = 'todos.json'
        self.UNTITLED_NAME = 'Untitled'


    def get_project_name(self):
        """Returns the project name"""
        try:
            with open(self.PROJECT_FILE, 'r') as project_file:
                data = json.load(project_file)
                name = data.get('name')
        except:
            return self.UNTITLED_NAME

        return name if name else self.UNTITLED_NAME


    def get_command_name(self):
        """Returns the typed command"""
        try:
            return '{} {}'.format(sys.argv[0], sys.argv[1])
        except:
            return sys.argv[0]


    def get_command_attributes(self):
        """Returns the attributes of the command"""
        try:
            return ' '.join(sys.argv[2:])
        except:
            return None


    def get_titles_input(self):
        """Returns all item titles typed by the user
        The user can type several titles separated by a comma"""
        titles_input = self.get_command_attributes()

        if not titles_input:
            print(
                '{info}Empty item ignored{reset}'
                .format(
                    info=Fore.INFO,
                    reset=Style.RESET_ALL,
                )
            )
            sys.exit()

        titles = titles_input.split(',')
        return [ title.strip() for title in titles if title is not '' ]


    def cancel_command(self):
        """Cancels the current command"""
        print(
            '\n{fail}{command}{reset} canceled'
            .format(
                command=self.get_command_name(),
                fail=Fore.FAIL,
                reset=Style.RESET_ALL
            )
        )
        sys.exit()


    def project_not_found(self):
        """Exits the program if no project found"""
        print(
            '{fail}No project found.{reset}'
            .format(
                fail=Fore.FAIL,
                reset=Style.RESET_ALL,
            )
        )
        sys.exit(1)


    def ask_create_project(self):
        """Asks to create a new project if none found"""
        try:
            answer = input(
                '{warning}No project found, create one first?{reset} (y/n) '
                .format(
                    warning=Fore.WARNING,
                    reset=Style.RESET_ALL,
                )
            ).lower()
        except KeyboardInterrupt:
            self.cancel_command()

        if answer.startswith('n'):
            sys.exit()

        from todo.commands.init import Init

        Init.run()


    def update_project(self, new_data):
        """Updates the project file with the new data"""
        try:
            with open(self.PROJECT_FILE, 'w', encoding='utf-8') as project_file:
                json.dump(
                    new_data,
                    project_file,
                    sort_keys=True,
                    indent=4,
                    ensure_ascii=False,
                )
        except:
            print(
                '{fail}An error has occured while updating the project{reset}'
                .format(
                    fail=Fore.FAIL,
                    reset=Style.RESET_ALL,
                )
            )
            sys.exit(1)
