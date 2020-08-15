import turtle
wn = turtle.Screen()
sam = turtle.Turtle()
sam.color('Red')
wn.bgcolor('Black')
sam.pensize('10')
distance = 50
angle = 90

for _ in range(16):
    sam.forward(distance)
    sam.left(angle)
    distance = distance + 10
    angle = angle + 5
wn.exitonclick()