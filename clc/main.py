#!/usr/bin/env python
import curses
import curses.textpad
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

        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)

        self.input_scr = self.screen.subwin(self.maxY - 1, 2)
        self.input_box = curses.textpad.Textbox(self.input_scr)

        self.output_pad = curses.newpad(400, 60)

        self.hint_scr = self.screen.subwin(1, self.maxX, self.maxY - 2, 0)
        self.hint_scr.bkgd(curses.color_pair(1))

        self._loop()

    def _loop(self):
        while self.running:
            self.render()

    def start(self):
        self.running = True
        curses.wrapper(self._start)

    def render(self):
        self.screen.addstr(self.maxY - 1, 0, '> ')
        self.hint_scr.addstr('this is a hint!')
        self.input_scr.clear()
        self.screen.refresh()
        self.output_pad.refresh(0, 0, 0, 1, 20, 30)

        try:
            equation = self.input_box.edit()
        except KeyboardInterrupt:
            self.running = False
        else:
            self.handle_input(equation)

    def handle_input(self, equation):
        try:
            result = 'ans = ' + str(self.clc.push(equation))
        except ValueError:
            result = "Could not parse input"
        self.output_pad.addstr(equation + '\n')
        self.output_pad.addstr(result + '\n\n')


def main():
    ui = ClcUI()
    ui.start()

if __name__ == "__main__":
    main()
