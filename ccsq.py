# Importing neccesary variables
import turtle as t
import time as tiempo

# Input for number of circles
'''
many_circles = int(input("How many circle(s) do you want to draw?\n\n"))
t.speed(0)
t.teleport(-400, 0)
for circle in range(many_circles):
    t.penup()
    t.forward(800//(many_circles+1))
    t.pendown()
    t.fillcolor("Black")
    t.begin_fill()
    t.circle(30)
    t.end_fill()

t.teleport(0,0)
tiempo.sleep(5)
'''

# Concurrent Squares
many_squares = 20 #int(input("How many squares do you want?\n"))
t.speed(0)
# Setting up to center
t.teleport(-200, 200)
colors = ['red', 'yellow', 'orange', 'green', 'blue', 'purple', 'purple', 'white', 'black']

# Making the squares outer loop, each square
for circle1 in range(many_squares):
    t.color(colors[circle1%(len(colors)-1)])
    t.begin_fill()
    # Inner loop, each side and turn
    for circle2 in range(4):
        t.forward((many_squares-circle1)*20)
        t.right(90)
    t.end_fill()
    # Moving inwards a bit more
    x, y = t.pos()
    x = round(x)
    y = round(y)
    t.teleport(x+10, y-10)

# Viewing the squares
tiempo.sleep(5)
