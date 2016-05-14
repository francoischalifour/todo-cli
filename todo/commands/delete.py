from __future__ import absolute_import

import os
import sys
import json

from todo.commands.base import Command
from todo.utils.styles import Fore, Style


class DeleteCommand(Command):
    def ask_confirmation(self, name):
        """Asks confirmation to delete the project"""
        sys.stdout.write(
            '{warning}Do you want to delete the project {green}{name}{warning}?{reset} (y/n) '
            .format(
                name=name,
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


    def delete_project(self):
        """Deletes the existing project"""
        try:
            os.remove(self.PROJECT_FILE)
        except FileNotFoundError:
            print(
                '{warning}No project exists.{reset}'
                .format(
                    warning=Fore.WARNING,
                    reset=Style.RESET_ALL,
                )
            )
            sys.exit()
        except:
            print(
                '{fail}Unable to delete the project.{reset}'
                .format(
                    fail=Fore.FAIL,
                    reset=Style.RESET_ALL,
                )
            )
            sys.exit()


    def run(self):
        name = self.get_project_name()
        self.ask_confirmation(name)
        self.delete_project()

        print(
            'The project {green}{name}{reset} has been deleted.'
            .format(
                name=name,
                green=Fore.GREEN,
                reset=Style.RESET_ALL,
            )
        )


Delete = DeleteCommand()
