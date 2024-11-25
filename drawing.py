import turtle
# assigning color to the square
turtle.pendown()
turtle.pencolor("purple")
turtle.fillcolor("purple")
turtle.begin_fill()

#looping to make a square
for i in range(5):
    turtle.forward(100)
    turtle.left(90)
    
turtle.end_fill()
turtle.penup()

turtle.left(90)
turtle.forward(200)

turtle.pendown()
turtle.pencolor("orange")
turtle.fillcolor("orange")
turtle.begin_fill()

for i in range(6):
    turtle.forward(100)
    turtle.left(360/6)

turtle.end_fill()
turtle.penup()

turtle.right(90)
turtle.forward(200)

turtle.pendown()
turtle.pencolor("blue")
turtle.fillcolor("blue")
turtle.begin_fill()

for i in range(2):
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    
    
turtle.end_fill()
turtle.penup()

turtle.right(180)
turtle.forward(400)

turtle.pendown()
turtle.pencolor("red")
turtle.fillcolor("red")
turtle.begin_fill()
for i in range(3):
    turtle.forward(100)
    turtle.left(360/6)
    turtle.forward(150)
    turtle.left(360/6)

turtle.end_fill()
turtle.penup()


    
