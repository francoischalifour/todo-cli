from __future__ import absolute_import

import os
import sys
import json

from todo.commands.base import Command
from todo.utils.styles import Fore, Style


FOLDER_NAME = os.getcwd().split('/')[-1]


class InitCommand(Command):
    def does_already_exist(self):
        """Checks if a project already exists"""
        if os.path.isfile(self.PROJECT_FILE):
            sys.stdout.write(
                '{warning}A project called {green}{name}{warning} already exists, erase it?{reset} (y/n) '
                .format(
                    name=self.get_project_name(),
                    green=Fore.GREEN,
                    warning=Fore.YELLOW,
                    reset=Style.RESET_ALL,
                )
            )
            try:
                answer = input().lower()
            except KeyboardInterrupt:
                self.cancel_command()

            if answer.startswith('n'):
                sys.exit()


    def get_new_project_name(self):
        """Returns the new project name typed by the user"""
        sys.stdout.write(
            '{blue}Project name{reset}: ({green}{name}{reset}) '
            .format(
                name=FOLDER_NAME,
                blue=Fore.BLUE,
                green=Fore.GREEN,
                reset=Style.RESET_ALL,
            )
        )
        try:
            name = input()
        except KeyboardInterrupt:
            self.cancel_command()
        return name if name else FOLDER_NAME


    def create_project(self, name):
        """Inits a todo project in the root folder"""
        try:
            with open(self.PROJECT_FILE, 'w', encoding='utf-8') as project_file:
                json.dump(
                    {
                        "name": name
                    },
                    project_file,
                    sort_keys = True,
                    indent = 4,
                    ensure_ascii=False,
                )
        except:
            print(
                '{fail}An error has occured while initializing the project{reset}'
                .format(
                    fail=Fore.FAIL,
                    reset=Style.RESET_ALL,
                )
            )
            sys.exit(1)


    def run(self):
        self.does_already_exist()
        name = self.get_new_project_name()
        self.create_project(name)

        print(
            'The project {green}{name}{reset} has been created.'
            .format(
                name=name,
                green=Fore.GREEN,
                reset=Style.RESET_ALL,
            )
        )


Init = InitCommand()
