import turtle
scn = turtle.Screen()
scn.bgcolor("pale turquoise")

turtle.
shelby = turtle.Turtle()
sheldon = turtle.Turtle()
conch = turtle.Turtle()

def house():
    for i in range(2):
        turtle.forward(300)
        turtle.right(90)
        turtle.forward(350)
        turtle.right(90)

def grass():
    for i in range(2):
        sheldon.forward(1450)
        sheldon.right(90)
        sheldon.forward(100)
        sheldon.right(90)

sheldon.penup()
sheldon.goto(-718,-325)
sheldon.pendown()
sheldon.color("lime green")
sheldon.begin_fill()
grass()
sheldon.end_fill()



turtle.penup()
turtle.goto(-20,-20)
turtle.color("papaya whip")
turtle.pendown()
turtle.begin_fill()
house()
turtle.end_fill()

turtle.exitonclick()
