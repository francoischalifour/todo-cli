# -*- coding: utf-8 -*-

import sys

def safe_print(s):
    """Encodes the output in utf-8 for Windows console"""
    try:
        print(s)
    except UnicodeEncodeError:
        print(
            s
            .replace('✓', '-') # change the checkmark symbol
            .encode('utf8')
            .decode(sys.stdout.encoding)
        )
