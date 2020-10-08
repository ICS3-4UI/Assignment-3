from tkinter import *
import random as rd
import math

WIDTH = 600
HEIGHT = 600
RADIUS = 60
ORIGIN = [WIDTH / 2, HEIGHT / 2]

myInterface = Tk()
screen = Canvas(myInterface, width=WIDTH, height=HEIGHT, background="white")
screen.pack()


def create_circle(x, y, r, screenName, color):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return screenName.create_oval(x0, y0, x1, y1, outline="", fill=color)


for i in range(20000):
    x = rd.randint(0, WIDTH)
    y = rd.randint(0, WIDTH)

    dist_from_origin = math.hypot(x - ORIGIN[0], y - ORIGIN[1])
    if dist_from_origin >= RADIUS:

        if dist_from_origin <= 2 * RADIUS:
            c = "orange"
        elif dist_from_origin <= 3 * RADIUS:
            c = "yellow"
        elif dist_from_origin <= 4 * RADIUS:
            c = "lime"
        elif dist_from_origin <= 5 * RADIUS:
            c = "blue"
        else:
            c = "purple4"
    else:
        c = "red"

    create_circle(x, y, 2, screen, c)
screen.mainloop()
