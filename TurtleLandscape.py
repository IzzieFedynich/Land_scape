import turtle
from turtle import Turtle

scn = turtle.Screen()
scn.bgcolor("pale turquoise")


shelby = turtle.Turtle()
shelby.speed(100)
shelby.turtlesize(.1)
sheldon = turtle.Turtle()
sheldon.speed(100)
sheldon.turtlesize(.1)
conch = turtle.Turtle()
conch.speed(100)
conch.turtlesize(.1)
snappy = turtle.Turtle()
snappy.speed(100)
snappy.turtlesize(.1)
Kale = turtle.Turtle()
Kale.speed(100)
Kale.turtlesize(.1)
Slug = turtle.Turtle()
Slug.speed(100)
Slug.turtlesize(.1)
fluffy = turtle.Turtle()
fluffy.speed(100)
fluffy.turtlesize(.1)

def house():
    for i in range(2):
        shelby.forward(300)
        shelby.right(90)
        shelby.forward(350)
        shelby.right(90)

def grass():
    for i in range(2):
        sheldon.forward(1450)
        sheldon.right(90)
        sheldon.forward(100)
        sheldon.right(90)

def door():
    for i in range(2):
        Kale.forward(90)
        Kale.left(90)
        Kale.forward(120)
        Kale.left(90)


sheldon.penup()
sheldon.goto(-718,-325)
sheldon.pendown()
sheldon.color("lime green")
sheldon.begin_fill()
grass()
sheldon.end_fill()

shelby.penup()
shelby.goto(-110,25)
shelby.color("papaya whip")
shelby.pendown()
shelby.begin_fill()
house()
shelby.end_fill()

conch.penup()
conch.goto(-110,25)
conch.pendown()
conch.color("salmon")
conch.begin_fill()
conch.left(45)
conch.forward(220)
conch.right(92)
conch.forward(214)
conch.right(133)
conch.forward(305)
conch.end_fill()

snappy.penup()
snappy.goto(-110,25)
snappy.color("Indian Red")
snappy.pendown()
snappy.pensize(25)
snappy.left(45)
snappy.backward(20)
snappy.forward(250)
snappy.right(95)
snappy.forward(246)

Kale.penup()
Kale.goto(0,-325)
Kale.pendown()
Kale.color("peru")
Kale.begin_fill()
door()
Kale.end_fill()

Slug.penup()
Slug.goto(15,-265)
Slug.pendown()
Slug.color("gold")
Slug.shape("circle")
Slug.begin_fill()
Slug.circle(5)
Slug.end_fill()
Slug.turtlesize(.8)

fluffy.penup()
fluffy.goto(-300,275)
fluffy.pendown()
fluffy.color("seashell")

fluffy.begin_fill()
fluffy.circle(60)
fluffy.forward(30)
fluffy.circle(40)
fluffy.forward(30)
fluffy.circle(33)
fluffy.backward(100)
fluffy.circle(70)
fluffy.backward(40)
fluffy.circle(50)
fluffy.end_fill

turtle.exitonclick()
