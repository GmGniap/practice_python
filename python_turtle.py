import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
alex = turtle.Turtle()
alex.color("blue")
alex.shape("turtle")

print(list(range(5, 60, 2)))
alex.up()
for col in range(5, 60, 2):
    alex.stamp()
    alex.forward(col)
    alex.right(24)
wn.exitonclick()
