"""
New Pacman script, using Tkinter's animation methods to avoid flickering, and OOP-Style
"""

from tkinter import *

WIDTH = 800
HEIGHT = 800
Pacman_RADIUS = 60


class Pacman(Frame):
    # Character init
    def create_pacman(self, screen, x, y, r):
        x, y, x1, y1 = x - r, y - r, x + r, y + r
        return screen.create_arc(x, y, x1, y1, start=self.angleOpen, extent=self.angleClose, fill='yellow', style=PIESLICE)

    def create_circle(self, x, y, r, screenName, color):
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return screenName.create_oval(x0, y0, x1, y1, outline="", fill=color)

    def characterAnimation(self):
        # Horizontal movement speed
        if self.frames % self.mouthSpeed == 0:
            self.mouth_angle()
            self.screen.itemconfig(self.Character, start=self.angleOpen, extent=self.angleClose)
        # Horizontal speed is controlled by frame speed
        if self.frames != 0:
            self.after(self.xSpeed, self.characterAnimation)

            # Pacman's current mouth position equals to current frame proportional to each cherries location.
            if self.frames % ((Pacman_RADIUS * 1.6) + self.xSpeed) == 0:
                self.screen.delete(self.cherries[self.current_cherry])
                self.current_cherry += 1

        # Set mouth move speed
        self.frames -= 1
        self.screen.move(self.Character, 1, 0)

    def mouth_angle(self):
        if self.angleOpen != 1:
            self.angleOpen = 1
            self.angleClose = 359
        else:
            self.angleOpen = 30
            self.angleClose = 360 - 2 * self.angleOpen

    def __init__(self, master=None):
        # Init with superclass
        Frame.__init__(self, master)

        # Init screen
        self.screen = Canvas(width=WIDTH, height=HEIGHT, background='black')
        self.screen.pack()

        # Game variables
        self.angleOpen = 1
        self.angleClose = 359
        self.mouthSpeed = 20
        self.xSpeed = 10

        # Cherries
        self.cherries = []
        self.cherries_x, self.cherries_y = [80], [HEIGHT / 2]
        self.cherries_amount = 10
        self.current_cherry = 0
        for i in range(self.cherries_amount):
            self.cherries.append(self.create_circle(self.cherries_x[i], self.cherries_y[i], 10, self.screen, "red"))
            self.cherries_x.append(int(self.cherries_x[-1]) + 100)
            self.cherries_y.append(HEIGHT / 2)

        self.Character = self.create_pacman(self.screen, 0, HEIGHT / 2, Pacman_RADIUS)

        self.frames = WIDTH

        self.characterAnimation()


tk = Tk()
tk.title("Pacman - New version")
tk.geometry(f"{WIDTH}x{HEIGHT}")

screen = Pacman(tk)
screen.mainloop()
