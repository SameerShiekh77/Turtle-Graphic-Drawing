import turtle
wn = turtle.Screen()
star = turtle.Turtle()
star.speed(4)
dist = 20
for _ in range(50):
    star.forward(dist)
    star.right(45)
    dist = dist + 5
    
wn.exitonclick()