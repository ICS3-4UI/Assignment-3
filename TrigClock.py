from time import sleep
from tkinter import *
from datetime import datetime
import math

WIDTH = 800
HEIGHT = 800
ORIGIN = [WIDTH / 2, HEIGHT / 2]

myInterface = Tk()
screen = Canvas(myInterface, width=WIDTH, height=HEIGHT, background="black")
myInterface.title("Trig Clock")
screen.pack()

clock_radius = WIDTH / 2 - 50
clock_circumference = 2 * math.pi * clock_radius
hour_num = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# Place hour number on screen
d_theta = 2 * math.pi / 12
theta = 0

for i in hour_num:
    text_x = ORIGIN[0] + clock_radius * math.sin(theta)
    text_y = ORIGIN[1] - clock_radius * math.cos(theta)
    theta += d_theta
    screen.create_text(text_x, text_y, text=i, font="Arial 25", fill="white")

# Dots between the hours
d_theta = 2 * math.pi / 60
theta = 0

for i in range(60):
    x = ORIGIN[0] + clock_radius * math.cos(theta)
    y = ORIGIN[1] - clock_radius * math.sin(theta)
    theta += d_theta

    # Skip if we have an hour number, because we don't need dots overlapping the number
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
    angle_correction = -90

    # Angle information
    hour_angle = (((hour % 12) + (minute / 60)) / 12) * 360 + angle_correction
    minute_angle = ((minute + (second / 60)) / 60) * 360 + angle_correction
    second_angle = ((second / 60) * 360) + angle_correction

    # Update second
    angle_in_radians = second_angle * math.pi / 180
    hand_length = clock_radius - 40
    end_x = ORIGIN[0] + hand_length * math.cos(angle_in_radians)
    end_y = ORIGIN[1] + hand_length * math.sin(angle_in_radians)
    secondHand = screen.create_line(ORIGIN, end_x, end_y, width=8, fill="blue")

    # Update minute
    angle_in_radians = minute_angle * math.pi / 180
    hand_length = clock_radius - 70
    end_x = ORIGIN[0] + hand_length * math.cos(angle_in_radians)
    end_y = ORIGIN[1] + hand_length * math.sin(angle_in_radians)
    minuteHand = screen.create_line(ORIGIN, end_x, end_y, width=13, fill="red")

    # Update hour
    angle_in_radians = hour_angle * math.pi / 180
    hand_length = clock_radius - 110
    end_x = ORIGIN[0] + hand_length * math.cos(angle_in_radians)
    end_y = ORIGIN[1] + hand_length * math.sin(angle_in_radians)
    hourHand = screen.create_line(ORIGIN, end_x, end_y, width=19, fill="green")

    # Animation
    screen.update()
    sleep(1)
    screen.delete(secondHand, minuteHand, hourHand)

screen.mainloop()
