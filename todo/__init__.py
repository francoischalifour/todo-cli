#!/usr/bin/env python3
# coding: utf-8

from __future__ import absolute_import

import sys

from todo.exceptions import TodoError
from todo.parser import Parser
from todo.commands import commands_dict


def check_python_version():
    if sys.version_info[0] < 3:
        from todo.utils.compatibility import safe_print
        from todo.utils.styles import Fore, Style
        safe_print(
'''
{fail}{bold}\tUh oh!{reset}
{warning}You need Python 3 to use this program. 😕
{info}Download Python: {blue}https://www.python.org/downloads
{info}Learn more: {blue}https://github.com/francoischalifour/todo-cli{reset}
'''
            .format(
                fail=Fore.FAIL,
                bold=Style.BOLD,
                warning=Fore.WARNING,
                info=Fore.INFO,
                blue=Fore.BLUE,
                reset=Style.RESET_ALL,
            )
        )
        sys.exit(1)


def main(args=None):
    check_python_version()

    parser = Parser()

    if args is None:
        args = sys.argv[1:]

    try:
        cmd_name, cmd_args = parser.parseopts(args)
    except TodoError as err:
        sys.stderr.write('{}\n'.format(err))
        sys.exit(1)

    return commands_dict[cmd_name]()


if __name__ == '__main__':
    sys.exit(main())
