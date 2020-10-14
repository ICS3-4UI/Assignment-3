from tkinter import *
import statistics

WIDTH = 800
HEIGHT = 800
D = 200

myInterface = Tk()
myInterface.title("Introspective Triangle")
screen = Canvas(myInterface, width=WIDTH, height=HEIGHT, background="black")
screen.pack()

try:
    repetition = int(input("How many repetition would you like? >> "))
except ValueError:
    while True:
        print("Invalid input, please input again!")
        try:
            repetition = int(input("How many repetition would you like? >> "))
            break
        except:
            pass


def midpoint(x, y):
    return [statistics.mean(k) for k in zip(x, y)]


# Vertices
p, p1, p2 = [WIDTH - 100, 0], [0, HEIGHT], [WIDTH, HEIGHT]

# Interchanging colour
colour = ["white", "blue"]

# Parent triangle (largest)
screen.create_polygon(p, p1, p2, fill=colour[0 % 2])

# Smaller triangles for the pattern
for i in range(repetition):
    screen.create_polygon(p, p1, p2, fill=colour[i % 2])

    # Duplicate the variable
    old_p = p
    old_p1 = p1
    old_p2 = p2
    p = midpoint(old_p1, old_p2)
    p1 = midpoint(old_p, old_p2)
    p2 = midpoint(old_p, old_p1)

screen.mainloop()
