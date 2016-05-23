# coding: utf-8
"""
Interactive menu to select items
"""

import curses


EXIT_KEYS = [113, 27, 127, 10]
SPACE_KEY = 32


def show_options(title=None, subtitle=None, items=[], callback=None):
    screen = curses.initscr()

    def get_action(subtitle):
        try:
            return subtitle.split(' ')[0].lower()
        except:
            return 'trigger'

    try:
        curses.start_color()
        curses.use_default_colors()

        curses.noecho()
        curses.curs_set(0)
        screen.keypad(1)

        curses.init_pair(1, curses.COLOR_BLUE, -1)
        highlighted = curses.color_pair(1)

        curses.init_pair(2, curses.COLOR_GREEN, -1)
        subtitle_style = curses.color_pair(2)

        curses.init_pair(3, curses.COLOR_BLACK, -1)
        info_style = curses.color_pair(3)

        current_pos = 0
        offset_y = 5

        while True:
            no_items = len(items) if len(items) < 10 else 10
            screen.refresh()

            screen.addstr(2, 7, title, curses.A_BOLD | highlighted)
            screen.addstr(3, 7, subtitle, subtitle_style)

            pos = 0

            for item in items[:10]:
                is_done = item.get('done')
                status = ' ✓ ' if is_done else ' x '

                if pos == current_pos:
                    screen.addstr(
                        pos + offset_y, 4, '❯ {}  {}'
                        .format(status, item['title']),
                        highlighted
                    )
                else:
                    screen.addstr(
                        pos + offset_y, 4, '  {}  {}'
                        .format(status, item['title'])
                    )

                pos += 1

            if len(items) > 10:
                screen.addstr(pos + offset_y, 4, '   ...', info_style)

            screen.addstr(pos + offset_y + 1, 7, 'space', curses.A_BOLD | info_style)
            screen.addstr(pos + offset_y + 1, 14, 'to {}'.format(get_action(subtitle)), info_style)
            screen.addstr(pos + offset_y + 2, 7, 'q', curses.A_BOLD | info_style)
            screen.addstr(pos + offset_y + 2, 14, 'to exit', info_style)

            key = screen.getch()

            screen.erase()

            if key == curses.KEY_DOWN:
                current_pos = current_pos + 1 if current_pos + 1 < no_items else 0
            elif key == curses.KEY_UP:
                current_pos = current_pos - 1 if current_pos > 0 else no_items - 1
            elif key == SPACE_KEY:
                items = callback(current_pos, items)
            elif key in EXIT_KEYS:
                return items
    finally:
        curses.endwin()
