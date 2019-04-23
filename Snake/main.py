import os,sys,time,random
import curses

screen = curses.initscr()
screen.clear()

scrh, scrw = screen.getmaxyx()
w = curses.newwin(scrh, scrw, 0, 0)
w.keypad(1)
w.timeout(100)

startx = int(scrw / 2)
starty = int(scrh / 2)

snake = [
    [starty, startx],
    [starty, startx - 1],
    [starty, startx - 2]
]

