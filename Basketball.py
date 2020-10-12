from time import sleep
from tkinter import *
import random as rd

WIDTH = 1000
HEIGHT = 800

myInterface = Tk()
myInterface.title("Granny Shot Competition")
screen = Canvas(myInterface, width=WIDTH, height=HEIGHT, background="sky blue")
screen.pack()


def create_circle(x, y, r, screenName, color):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return screenName.create_oval(x0, y0, x1, y1, outline="", fill=color)


# Floor
top_right, bottom_left = [0, 525], [WIDTH, HEIGHT]
screen.create_rectangle(top_right, bottom_left, fill="grey", outline="")

# Sun
create_circle(900, 100, 80, screen, "gold")

# Clouds

# Different cloud colours to create a 3D feel to it.
c_clr = ["snow", "azure", "light cyan", "white"]

for c in range(rd.randint(100, 120)):
    x = rd.randint(300, 500)
    y = rd.randint(75, 125)
    size = rd.randint(30, 50)
    create_circle(x, y, size, screen, color=rd.choice(c_clr))

for c in range(rd.randint(80, 100)):
    x = rd.randint(800, 1000)
    y = rd.randint(155, 215)
    size = rd.randint(30, 50)
    create_circle(x, y, size, screen, color=rd.choice(c_clr))

for c in range(rd.randint(60, 80)):
    x = rd.randint(550, 630)
    y = rd.randint(300, 325)
    size = rd.randint(10, 30)
    screen.create_oval(x, y, x + size, y + size, fill=rd.choice(c_clr), outline="white")

# Basketball net
screen.create_rectangle(685, 385, 724, 386, width=3, outline="brown")

n_tl, n_br = [725, 300], [735, 675]
screen.create_rectangle(n_tl, n_br, fill="white", outline="")

colour = ["black", "silver", "grey", "slategray"]
# Asphalt
for i in range(500):
    x = rd.randint(0, WIDTH)
    y = rd.randint(525, HEIGHT)
    s = rd.randint(1, 4)
    c = rd.choice(colour)
    a = screen.create_oval(x, y, x + s, y + s, fill=c, outline="")

# Strings
screen.create_line(610, 381, 620, 450, fill="white", width=3)
screen.create_line(680, 390, 670, 450, fill="white", width=3)
# Diag lines
screen.create_line(610, 390, 676, 420, fill="white", width=3)
screen.create_line(615, 410, 671, 431, fill="white", width=3)
screen.create_line(620, 450, 671, 439, fill="white", width=3)
screen.create_line(617, 430, 669, 445, fill="white", width=3)
screen.create_line(675, 400, 613, 410, fill="white", width=3)
screen.create_line(671, 420, 618, 430, fill="white", width=3)

tl, br = [610, 375], [685, 395]
screen.create_oval(tl, br, fill="", outline="brown", width="2")

# Ring
screen.create_oval(550, 550, 800, 750, outline="red", width=10)
create_circle(550, 650, 20, screen, "red")

# Cover unnecessary ring
screen.create_rectangle(735, 550, 810, 700, fill="grey", outline="")
screen.create_rectangle(725, 550, 735, 575, fill="white", outline="")
screen.create_rectangle(800, 600, 810, 675, fill="grey", outline="")
screen.create_rectangle(725, 700, 800, 750, fill="grey", outline="")

colour = ["black", "silver", "grey", "slategray"]
# Asphalt
for i in range(30):
    x = rd.randint(730, 810)
    y = rd.randint(525, HEIGHT)
    s = rd.randint(1, 4)
    c = rd.choice(colour)
    a = screen.create_oval(x, y, x + s, y + s, fill=c, outline="")

# Floor line
screen.create_rectangle(175, 525, 200, 800, fill="white", outline="")

##Player
# Hair
screen.create_arc(70, 550, 180, 420, start=20, extent=180, fill="Saddle Brown", outline="")
# Head
create_circle(125, 475, 40, screen, "bisque")
screen.create_rectangle(125, 519, 125, 625, fill="", outline="black", width="4")

# Legs
screen.create_polygon(125, 625, 90, 700, outline="black", width="4")
screen.create_polygon(125, 625, 160, 700, outline="black", width="4")

# Arms
arm_1x, arm_2x = 225, 225
arm_1y, arm_2y = 500, 515
original_arm_coord = [arm_1x, arm_2x, arm_1y, arm_2y]

# Face features
eye1, eye2 = create_circle(120, 460, 5, screen, "black"), create_circle(145, 460, 5, screen, "black")
pupils = create_circle(121, 461, 3, screen, "white"), create_circle(146, 461, 3, screen, "white")
mouth = screen.create_polygon(120, 490, 130, 500, 140, 490, width=3)

# Sign
screen.create_rectangle(900, 600, 910, 800, fill="light gray", outline="")
screen.create_rectangle(800, 400, 1000, 600, fill="light gray", outline="")
screen.create_text(900, 500, text="Granny Shot\nCompetition", font="Consolas 20")
# Ball
bx, by = 220, 500
b_radius = 30


## Debugging purposes
# Grid lines
def createGridLine(spacing):
    for x in range(0, 1000, spacing):
        screen.create_line(x, 25, x, 1000, fill="blue")
        screen.create_text(x, 5, text=str(x), font="Times 9", anchor=N)

    for y in range(0, 1000, spacing):
        screen.create_line(25, y, 1000, y, fill="blue")
        screen.create_text(5, y, text=str(y), font="Times 9", anchor=W)


# createGridLine(25)

xSpeed = 0.1
ySpeed = 0.3
gravity = 0.2
xStart, yStart = 0, 0
bounce_count = 50
upward_force = 70

eye_c = ["white", "white", "white", "black", "black", "black"]

## Animations
for f in range(200):
    arm1 = screen.create_polygon(125, 550, arm_1x, arm_1y, outline="black", width="4")
    arm2 = screen.create_polygon(125, 570, arm_2x, arm_2y, outline="black", width="4")
    create_circle(121, 461, 3, screen, eye_c[f % 6]), create_circle(146, 461, 3, screen, eye_c[f % 6])

    if f < 20:
        basketball = create_circle(bx, by, b_radius, screen, "brown")
        arm_1y -= 3
        arm_2y -= 3
        arm_1x -= 4
        arm_2x -= 4
        bx = arm_2x
        by = arm_2y
    if f > 20 and not (bx + b_radius > tl[0] + 60):
        bx = 8.5 * (f - 20) + arm_2x
        by = .2 * (f - 20) ** 2 - 13 * (f - 20) + arm_2y
        basketball = create_circle(bx, by, b_radius, screen, "brown")

    else:
        if bx + b_radius > tl[0] + 60 and bounce_count > 0:
            basketball = create_circle(bx, by, b_radius, screen, "brown")
            by += 15

            if by - b_radius >= 600:
                by -= bounce_count
                bounce_count -= 3
        elif bounce_count <= 0:
            basketball = create_circle(bx, by, b_radius, screen, "brown")
            break

    screen.update()
    sleep(0.03)
    screen.delete(arm1, arm2, basketball)

basketball = create_circle(bx, by, b_radius, screen, "brown")

screen.delete(arm1, arm2)
for f in range(50):
    arm1 = screen.create_polygon(125, 550, arm_1x, arm_1y, outline="black", width="4")
    arm2 = screen.create_polygon(125, 570, arm_2x, arm_2y, outline="black", width="4")

    arm_1y += 3
    arm_2y += 3

    screen.update()
    sleep(0.03)
    screen.delete(arm1, arm2)

arm1 = screen.create_polygon(125, 550, arm_1x, arm_1y, outline="black", width="4")
arm2 = screen.create_polygon(125, 570, arm_2x, arm_2y, outline="black", width="4")
screen.mainloop()
