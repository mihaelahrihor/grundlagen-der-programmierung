import turtle
def rechteck():


    plansa = turtle.getscreen()

    #patrat
    """
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    """

    # dreptunghi

    turtle.color("blue")
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(100)

    turtle.penup()
    turtle.goto(100, 70)
    turtle.pendown()

    turtle.color("red")
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(25)

    plansa.exitonclick()







