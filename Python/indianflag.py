import turtle
turtle.bgcolor('black')
wn=turtle.Screen()
tr=turtle.Turtle()

move=1
tr.speed("fastest")
for i in range (360):
   
    tr.write("Welcome ",'false','center',font=('Showcard gothic',50))
    tr.penup()
    tr.goto(-200,100)
    tr.pendown()
    tr.color("orange")
    tr.right(move)
    tr.forward(100)
    tr.penup()
    tr.color("white")
    tr.pendown()
    tr.right(30)
    tr.forward(60)
    tr.pendown()
    tr.color("light green")
    tr.left(10)
    tr.forward(50)
    tr.right(70)
    tr.penup()
    tr.pendown()
    tr.color('light blue')
    tr.forward(50)
    tr.color('light green')
    tr.pu()
    tr.pd()
    tr.color("light blue")
    tr.forward(100)
    tr.color('brown')
    tr.forward(200)
    tr.pu()
    tr.pd()
    tr.color('light green')
    tr.circle(2)
    tr.color('light blue')
    tr.circle(4)
    tr.pu()
    tr.fd(20)
    tr.pd()
    tr.circle(6)
    tr.pu()
    tr.fd(40)
    tr.pd()
    tr.circle(8)
    tr.pu()
    tr.fd(80)
    tr.pd()
    tr.circle(10)
    tr.pu()
    tr.fd(120)
    tr.pd()
    tr.circle(20)
    tr.color('yellow')
    tr.circle(10)
    tr.pu()
    tr.pd()
    tr.color('white')
    tr.forward(150)
    tr.color('red')
    tr.fd(50)
    tr.color ('blue')
    tr.begin_fill()
    tr.penup()
    tr.home()
    move=move+1
tr.penup()
tr.forward(100)
turtle.done()