import turtle

wn = turtle.Screen()
wn.bgcolor('Skyblue')
dijkstra = turtle.Turtle()
dijkstra.color('Red')
dijkstra.pensize(20)
dijkstra.shape('circle')
for i in range(8):
    dijkstra.forward(75)
    dijkstra.left(360/8)

wn.exitonclick()