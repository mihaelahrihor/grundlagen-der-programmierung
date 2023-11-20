import turtle
t=turtle.Turtle()

#A
''''
t.penup()
t.goto(-30,50) #centering in the screen
t.pendown()


t.right(65)
t.forward(100)

t.setpos(-30,50)
t.right(50)
t.forward(100)

t.penup()
t.setpos(-50,-10)
t.right(65)
t.pendown()
t.backward(50)
'''

#B
#draw straight line
t.goto(-30,50) #centering in the screen
t.pendown()

t.right(90)
t.forward(200)

t.penup()
t.goto(-30,50) #centering in the screen
#draw first curve
t.pendown()
t.right(-90)
t.circle(-50,180)


t.penup()
t.goto(-30,-50) #centering in the screen
#draw second curve
t.pendown()
t.right(180)
t.circle(-50,180)