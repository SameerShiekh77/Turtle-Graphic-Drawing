import turtle

wn = turtle.Screen()
wn.bgcolor('Skyblue')
dijkstra = turtle.Turtle()
dijkstra.color('Red')
dijkstra.pensize(20)
dijkstra.shape('turtle')
for i in range(6):
    dijkstra.forward(100)
    dijkstra.left(360/6)

wn.exitonclick()