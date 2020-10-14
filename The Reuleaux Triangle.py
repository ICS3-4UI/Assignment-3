from tkinter import *
from math import *

WIDTH = 800
HEIGHT = 800
ORIGIN = [WIDTH / 2, HEIGHT / 2]

myInterface = Tk()
myInterface.title("The Reuleaux Triangle")
screen = Canvas(myInterface, width=WIDTH, height=HEIGHT, background="black")
screen.pack()


def draw_reuleaux_arc(screenVar, x, y, r):
    # Get the coordinates of the top vertices
    x1 = x + r / 2
    y1 = y - r * sin(radians(60))
    screenVar.create_arc(x - r, y - r, x + r, y + r, extent=60, fill="red", outline="")
    screenVar.create_arc(x, y - r, x + r + r, y + r, start=120, extent=60, fill="green", outline="")
    screenVar.create_arc(x1 - r, y1 - r, x1 + r, y1 + r, start=240, extent=60, fill="blue", outline="")


L = 400
draw_reuleaux_arc(screen, ORIGIN[0] - L / 2, ORIGIN[1] + L / 3, 400)

screen.mainloop()
