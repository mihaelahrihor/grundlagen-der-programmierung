
import turtle

def hauser():
    # Setarea ecranului
    plansa = turtle.getscreen()
    plansa.bgcolor("white")

    # Crearea unui obiect Turtle pentru prima casă
    house1 = turtle.Turtle()
    house1.shape("turtle")
    house1.color("blue")
    house1.speed(1)

    # Desenarea primei case
    house1.begin_fill()
    house1.fillcolor("blue")
    house1.goto(-100, 0)
    house1.goto(-100, -100)
    house1.goto(0, -100)
    house1.goto(0, 0)
    house1.end_fill()

    # Desenarea ușii primei case
    house1.penup()
    house1.goto(-40, -100)
    house1.pendown()

    house1.begin_fill()
    house1.fillcolor("brown")
    house1.goto(-40, 0)
    house1.goto(-20, 0)
    house1.goto(-20, -100)
    house1.end_fill()

    # Desenarea ferestrei primei case
    house1.penup()
    house1.goto(-80, -30)
    house1.pendown()
    house1.begin_fill()
    house1.fillcolor("yellow")
    house1.goto(-80, 0)
    house1.goto(-50, 0)
    house1.goto(-50, -30)
    house1.end_fill()

    # Desenarea acoperișului în formă de triunghi pentru prima casă
    house1.penup()
    house1.goto(-110, 0)
    house1.pendown()
    house1.begin_fill()
    house1.fillcolor("red")
    house1.goto(0, 50)
    house1.goto(10, 0)
    house1.end_fill()

    # Crearea unui obiect Turtle pentru a doua casă
    house2 = turtle.Turtle()
    house2.shape("turtle")
    house2.color("green")
    house2.speed(1)

    # Desenarea celei de-a doua case
    house2.penup()
    house2.goto(50, 0)
    house2.pendown()

    house2.begin_fill()
    house2.fillcolor("green")
    house2.goto(50, -100)
    house2.goto(150, -100)
    house2.goto(150, 0)
    house2.end_fill()

    # Desenarea ușii celei de-a doua case
    house2.penup()
    house2.goto(110, -100)
    house2.pendown()
    house2.begin_fill()
    house2.fillcolor("brown")
    house2.goto(110, 0)
    house2.goto(130, 0)
    house2.goto(130, -100)
    house2.end_fill()

    # Desenarea ferestrei celei de-a doua case
    house2.penup()
    house2.goto(70, -30)
    house2.pendown()
    house2.begin_fill()
    house2.fillcolor("yellow")
    house2.goto(70, 0)
    house2.goto(100, 0)
    house2.goto(100, -30)
    house2.end_fill()

    # Desenarea acoperișului în formă de triunghi pentru a doua casă
    house2.penup()
    house2.goto(60, 0)
    house2.pendown()
    house2.begin_fill()
    house2.fillcolor("red")
    house2.goto(160, 50)
    house2.goto(170, 0)
    house2.end_fill()

    # Închiderea ferestrei la clic
    plansa.exitonclick()