from time import sleep
from tkinter import *
import random as rd
from datetime import datetime
import math

WIDTH = 800
HEIGHT = 800
ORIGIN = [WIDTH / 2, HEIGHT / 2]

myInterface = Tk()
screen = Canvas(myInterface, width=WIDTH, height=HEIGHT, background="black")
myInterface.title("Trig Clock")
screen.pack()


def create_circle(x, y, r, screenName, color="", out="", w="", d=""):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return screenName.create_oval(x0, y0, x1, y1, outline=out, fill=color, width=w, dash=d)


clock_radius = WIDTH / 2 - 50
clock_circumference = 2 * math.pi * clock_radius
hour_num = [3, 2, 1, 12, 11, 10, 9, 8, 7, 6, 5, 4]

# Place hour number on screen
d_theta = 2 * math.pi / 12
theta = 0

for i in hour_num:
    text_x = ORIGIN[0] + clock_radius * math.cos(theta)
    text_y = ORIGIN[1] - clock_radius * math.sin(theta)
    theta += d_theta
    screen.create_text(text_x, text_y, text=i, font="Arial 25", fill="white")

# Dots between the hours
d_theta = 2 * math.pi / 60
theta = 0

for i in range(60):
    x = ORIGIN[0] + clock_radius * math.sin(theta)
    y = ORIGIN[1] - clock_radius * math.cos(theta)
    theta += d_theta
    if i % 5 == 0:
        continue
    else:
        screen.create_oval(x, y, x + 6, y + 6, fill="white")

while True:
    # Time info
    hour = datetime.now().hour
    minute = datetime.now().minute
    second = datetime.now().second

    # Tkinter angle correction
    ac = -90

    # Angle information
    hour_angle = (((hour % 12) + (minute / 60)) / 12) * 360 + ac
    minute_angle = ((minute + (second / 60)) / 60) * 360 + ac
    second_angle = ((second / 60) * 360) + ac

    # Update second
    angle_in_radians = second_angle * math.pi / 180
    hand_length = clock_radius - 40

    end_x = ORIGIN[0] + hand_length * math.cos(angle_in_radians)
    end_y = ORIGIN[1] + hand_length * math.sin(angle_in_radians)
    secondhand = screen.create_line(ORIGIN, end_x, end_y, width=10, fill="blue")

    # Update minute
    angle_in_radians = minute_angle * math.pi / 180
    hand_length = clock_radius - 70
    end_x = ORIGIN[0] + hand_length * math.cos(angle_in_radians)
    end_y = ORIGIN[1] + hand_length * math.sin(angle_in_radians)
    minutehand = screen.create_line(ORIGIN, end_x, end_y, width=13, fill="red")

    # Update hour
    angle_in_radians = hour_angle * math.pi / 180
    hand_length = clock_radius - 110
    end_x = ORIGIN[0] + hand_length * math.cos(angle_in_radians)
    end_y = ORIGIN[1] + hand_length * math.sin(angle_in_radians)
    hourhand = screen.create_line(ORIGIN, end_x, end_y, width=16, fill="green")
    screen.update()
    sleep(1)
    screen.delete(secondhand, minutehand, hourhand)

screen.mainloop()
