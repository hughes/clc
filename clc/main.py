#!/usr/bin/env python
import curses
import curses.textpad
import time
from clc import Clc

class ClcUI():
    def __init__(self):
        self.screen = None
        self.input_scr = None
        self.running = False
        self.maxY = None
        self.maxX = None

        self.clc = Clc()

    def _start(self, stdscr):
        self.screen = stdscr
        self.maxY, self.maxX = self.screen.getmaxyx()
        self.input_scr = self.screen.subwin(self.maxY-1, 2)
        self.hint_scr = self.screen.subwin(self.maxY-2, 0)

        self._loop()

    def _loop(self):
        while self.running:
            self.render()

    def start(self):
        self.running = True
        curses.wrapper(self._start)

    def render(self):
        self.screen.addstr(self.maxY-1, 0, '> ')
        self.hint_scr.addstr('this is a hint!')
        self.input_pad = curses.textpad.Textbox(self.input_scr)
        self.screen.refresh()
        try:
            equation = self.input_pad.edit()
        except KeyboardInterrupt:
            self.running = False
        else:
            self.clc.push(equation)

def main():
    ui = ClcUI()
    ui.start()

if __name__ == "__main__":
    main()

