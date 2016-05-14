#!/usr/bin/env python3
# coding: utf-8

from __future__ import absolute_import

import sys

from todo.exceptions import TodoError
from todo.parser import Parser
from todo.commands import commands_dict


def main(args=None):
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
