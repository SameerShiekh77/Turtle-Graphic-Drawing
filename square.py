import turtle
wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color('Red')
alex.pensize(width=10)

alex.forward(50)                 # make alex draw a square
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

wn.exitonclick()
