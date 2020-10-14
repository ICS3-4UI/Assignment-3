"""
New Pacman script, using Tkinter's animation methods to avoid flickering, and OOP-Style
"""

from tkinter import *

WIDTH = 800
HEIGHT = 800
Pacman_RADIUS = 60


class Pacman(Frame):
    # Creates a circular arc
    def create_pacman(self, screen, x, y, r):
        return screen.create_arc(x - r, y - r, x + r, y + r, fill='yellow', style=PIESLICE, start=self.angleOpen, extent=self.angleClose)

    def create_circle(self, x, y, r, screenName, color):
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return screenName.create_oval(x0, y0, x1, y1, outline="", fill=color)

    def mouth_angle(self):
        if self.angleOpen == 1:
            self.angleOpen = 30
            self.angleClose = 360 - 2 * self.angleOpen
        else:
            self.angleOpen = 1
            self.angleClose = 359

    def moveCharacter(self):
        # Set mouth move speed
        self.frames -= 1
        self.canvas.move(self.Character, 1, 0)
        # Horizontal movement speed
        if self.frames % self.mouthSpeed == 0:
            self.mouth_angle()
            self.canvas.itemconfig(self.Character, start=self.angleOpen, extent=self.angleClose)
        # Horizontal speed is controlled by frame speed
        if self.frames != 0:
            self.after(self.xSpeed, self.moveCharacter)

            # Pacman's current mouth position equals to current frame proportional to each cherries location.
            if self.frames % ((Pacman_RADIUS * 1.6) + self.xSpeed) == 0:
                self.canvas.delete(self.cherries[self.current_cherry])
                self.current_cherry += 1

    def __init__(self, master=None):
        # Init with superclass
        Frame.__init__(self, master)

        self.angleOpen = 1
        self.angleClose = 359
        self.mouthSpeed = 20
        self.xSpeed = 10

        # Init screen
        self.canvas = Canvas(width=WIDTH, height=HEIGHT, background='black')
        self.canvas.pack()

        # Cherries
        self.cherries = []
        self.cherries_x, self.cherries_y = [80], [HEIGHT / 2]
        self.cherries_amount = 10
        self.current_cherry = 0
        for i in range(self.cherries_amount):
            self.cherries.append(self.create_circle(self.cherries_x[i], self.cherries_y[i], 10, self.canvas, "red"))
            self.cherries_x.append(int(self.cherries_x[-1]) + 100)
            self.cherries_y.append(HEIGHT / 2)

        self.Character = self.create_pacman(self.canvas, 0, HEIGHT / 2, Pacman_RADIUS)

        self.frames = WIDTH

        self.moveCharacter()


tk = Tk()
tk.title("Pacman - New version")
tk.geometry(f"{WIDTH}x{HEIGHT}")

screen = Pacman(master=tk)
screen.mainloop()
