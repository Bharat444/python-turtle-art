
import turtle

turtle.Screen().bgcolor("white")

t = turtle.Turtle()

t.pensize(5)

# Left foot
t.penup()
t.goto(-40,-50)
t.pendown()
t.seth(-90)

t.fillcolor("black")
t.begin_fill()
t.forward(150)
t.seth(180)
t.forward(100)
t.circle(-30,180)
t.forward(50)
t.seth(90)
t.forward(90)
t.end_fill()

# Right foot
t.penup()
t.goto(40,-50)
t.pendown()
t.seth(-90)

t.begin_fill()
t.forward(150)
t.seth(0)
t.forward(100)
t.circle(30,180)
t.forward(50)
t.seth(90)
t.forward(90)
t.end_fill()

# Left hand
t.penup()
t.goto(-140,90)
t.seth(-150)
t.pendown()

t.fillcolor("yellow")
t.begin_fill()
t.forward(90)
t.seth(-40)
t.forward(70)

t.seth(-130)
t.forward(30)
t.seth(140)
t.forward(120)
t.seth(30)
t.forward(160)
t.end_fill()

t.penup()
t.goto(-140,90)
t.seth(-150)
t.pendown()
t.forward(90)

t.fillcolor("black")

t.seth(-40)
t.forward(70)
t.seth(40)
t.begin_fill()
t.forward(30)
t.seth(-40)
t.forward(10)
t.circle(-50,180)
t.circle(-20,180)
t.seth(140)
t.forward(20)
t.end_fill()

# Right hand
t.penup()
t.goto(140,90)
t.seth(60)
t.pendown()

t.fillcolor("yellow")
t.begin_fill()
t.forward(150)
t.seth(150)
t.forward(30)
t.seth(-120)
t.forward(100)
t.end_fill()

t.backward(100)
t.seth(150)
t.backward(30)

t.fillcolor("black")
t.begin_fill()
t.seth(-30)
t.forward(20)
t.seth(90)
t.forward(30)
t.seth(30)
t.forward(40)
t.circle(15,180)
t.seth(80)
t.forward(10)
t.circle(20,180)
t.seth(90)
t.circle(15,180)
t.forward(50)
t.seth(-170)
t.forward(20)
t.seth(-30)
t.forward(50)
t.end_fill()

# Main Body
t.penup()
t.goto(-140,40)
t.seth(-90)
t.pendown()

t.fillcolor("yellow")

t.begin_fill()
t.circle(140,180)
t.forward(250)
t.circle(140,180)
t.forward(250)
t.end_fill()

t.fillcolor("blue")
t.begin_fill()
t.circle(140,180)
t.seth(180)
t.forward(90)
t.seth(90)
t.forward(50)
t.seth(0)
t.forward(90)
t.seth(90)
t.forward(30)
t.seth(180)
t.forward(280)
t.seth(-90)
t.forward(30)
t.seth(0)
t.forward(90)
t.seth(-90)
t.forward(50)
t.seth(180)
t.forward(90)
t.end_fill()

# Glass
t.penup()
t.seth(0)
t.goto(-140,270)
t.pendown()

t.pencolor("black")
t.pensize(30)
t.forward(280)

t.pensize(5)
t.fillcolor("white")
t.penup()
t.goto(70,220)
t.pendown()

t.begin_fill()
t.circle(50)
t.end_fill()

t.penup()
t.goto(70,250)
t.pendown()

t.fillcolor("black")
t.begin_fill()
t.circle(20)
t.end_fill()

t.fillcolor("white")
t.penup()
t.goto(-70,220)
t.pendown()

t.begin_fill()
t.circle(50)
t.end_fill()

t.penup()
t.goto(-70,250)
t.pendown()

t.fillcolor("black")
t.begin_fill()
t.circle(20)
t.end_fill()

t.hideturtle()
turtle.done()