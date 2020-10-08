"""
Using loops to animate causes flickering
"""

from time import sleep
from tkinter import *
import random as rd
import math

WIDTH = 800
HEIGHT = 800

myInterface = Tk()
screen = Canvas(myInterface, width=WIDTH, height=HEIGHT, background="black")
screen.pack()


def create_circle(x, y, r, screenName, color):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return screenName.create_oval(x0, y0, x1, y1, outline="", fill=color)


def draw_arc(screenName, x, y, r, **kwargs):
    if "start" in kwargs and "end" in kwargs:
        kwargs["extent"] = kwargs["end"] - kwargs["start"]
        del kwargs["end"]
    return screenName.create_arc(x - r, y - r, x + r, y + r, fill="yellow", **kwargs)


cherries = []
cherries_radius = 20
cherry_x, cherry_y = [300], [200]
# cherries
for n in range(5):
    cherries.append(create_circle(cherry_x[n], cherry_y[n], cherries_radius, screen, "red"))
    cherry_x.append(int(cherry_x[-1]) + 100)
    cherry_y.append(200)

Original_START = 30
START = Original_START
CLOSE_SPEED = 5
x, y = 100, 200
RADIUS = 100
currentcherry = 0

while x + RADIUS != WIDTH:
    EXTENT = 360 - 2 * START
    pacman = draw_arc(screen, x, y, RADIUS, start=START, extent=EXTENT)

    if START <= Original_START:
        START -= CLOSE_SPEED

    if START == 0:
        CLOSE_SPEED = -CLOSE_SPEED
    elif START == Original_START:
        CLOSE_SPEED = -CLOSE_SPEED

    for cx in cherry_x:
        if x == cx - cherries_radius:
            screen.delete(cherries[currentcherry])
            currentcherry += 1

    x += 10
    screen.update()
    screen.delete(pacman)
    sleep(0.05)

pacman = draw_arc(screen, x, y, RADIUS, start=START, extent=EXTENT)

screen.mainloop()
