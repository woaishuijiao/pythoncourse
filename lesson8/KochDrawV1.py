#KochDrawV1.py
import turtle
def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:  
            turtle.left(angle)
            koch(size/3, n-1)
turtle.setup(800, 800)
turtle.penup()
turtle.goto(-300, 150)
turtle.pendown()
turtle.pensize(3)
turtle.pencolor("purple")
level = 3
for i in range(0, 3):
    koch(600, level)
    turtle.right(120)
turtle.done()