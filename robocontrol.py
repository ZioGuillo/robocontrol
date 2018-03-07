#!/usr/bin/python

import rrb3 as rrb
import curses

rr = rrb.RRB3(6, 3)


# def confirm(question):
#     answer = raw_input(question)


# def test_motors():

#     rr.set_motors(0, 0, 0, 0)
#     rr.set_motors(1, 0, 1, 0)
#     confirm("confirm to stop")
#     rr.set_motors(0, 0, 0, 0)
#     print("test pass")

# test_motors()


screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)


try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            break
        elif char == curses.KEY_UP:
            rr.set_motors(1, 0, 1, 0)
        elif char == curses.KEY_DOWN:
            rr.set_motors(1, 1, 1, 1)
        elif char == curses.KEY_RIGHT:
            rr.set_motors(0.5, 1, 0.5, 0)
        elif char == curses.KEY_LEFT:
            rr.set_motors(0.5, 0, 0.5, 1)
        elif char == curses.KEY_BACKSPACE:
            rr.set_motors(0, 0, 0, 0)

finally:
    # Close down curses properly, inc turn echo back on!
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()
