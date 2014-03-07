#!/usr/bin/env python
import curses
import curses.textpad
import time

class ClcUI():
    def __init__(self):
        self.screen = None
        self.input_scr = None

    def _start(self, stdscr):
        self.screen = stdscr
        maxY, maxX = self.screen.getmaxyx()
        self.input_scr = self.screen.subwin(maxY-1, 0)
        self.hint_scr = self.screen.subwin(maxY-2, 0)

        self._loop()

    def _loop(self):
        self.render()
        time.sleep(1)

    def start(self):
        curses.wrapper(self._start)

    def render(self):
        self.input_scr.addstr('waiting for input')
        self.hint_scr.addstr('this is a hint!')
        self.screen.refresh()

def main():
    ui = ClcUI()
    ui.start()

if __name__ == "__main__":
    main()

