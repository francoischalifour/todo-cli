from __future__ import absolute_import

import sys

from todo.exceptions import CommandError
from todo.commands import commands_dict
from todo.utils.styles import Fore, Style


class Parser:
    def print_help(self):
        print(
            '{fail}usage: {blue}{prog} {green}<command>{reset} [options]'
            .format(
                prog='todo',
                fail=Fore.FAIL,
                blue=Fore.BLUE,
                green=Fore.GREEN,
                reset=Style.RESET_ALL,
            )
        )


    def parseopts(self, args):
        try:
            cmd_name = args[0]
            cmd_args = args[1:]
        except IndexError:
            self.print_help()
            sys.exit()

        if cmd_name not in commands_dict:
            msg = '{fail}unknown command {blue}{cmd}{reset}'.format(
                    cmd=cmd_name,
                    fail=Fore.FAIL,
                    blue=Fore.BLUE,
                    reset=Style.RESET_ALL,
                )
            raise CommandError(msg)

        return cmd_name, cmd_args


    def autocomplete(self):
        # TODO
        pass
