from __future__ import absolute_import

import os
import sys


if sys.version_info[0] < 3:
    from todo.utils.styles import Fore, Style
    sys.stderr.write(
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


if __package__ == '':
    path = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, path)


import todo


if __name__ == '__main__':
    sys.exit(todo.main())
