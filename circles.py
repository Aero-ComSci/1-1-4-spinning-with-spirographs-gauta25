import turtle as t
import time as tiempo
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
