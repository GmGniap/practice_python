import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
alex = turtle.Turtle()
alex.color("blue")
alex.shape("turtle")

'''print(list(range(5, 60, 2)))
alex.up()
for col in range(5, 60, 2):
    alex.stamp()
    alex.forward(col)
    alex.right(24)
wn.exitonclick()'''


alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(100)

wn.exitonclick()
