import curses, time, random, os, sys

screen = curses.initscr
screen.clear()

sh, sw = screen.getmaxyx()
w = curses.newwin(scrh, scrw, 0, 0)
w.keypad(1)
w.timeout(100)