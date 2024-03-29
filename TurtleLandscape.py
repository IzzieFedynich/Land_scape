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
shatter = turtle.Turtle()
shatter.speed(100)
shatter.turtlesize(.1)
leif = turtle.Turtle()
leif.speed(10)
leif.turtlesize(.1)

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

def cloud():
    for i in range(1):
        fluffy.begin_fill()
        fluffy.circle(60)
        fluffy.forward(30)
        fluffy.circle(40)
        fluffy.forward(30)
        fluffy.circle(33)
        fluffy.backward(100)
        fluffy.circle(70)
        fluffy.backward(50)
        fluffy.circle(50)
        fluffy.backward(45)
        fluffy.circle(30)
        fluffy.end_fill()

def window():
    for i in range(4):
        shatter.right(90)
        shatter.forward(75)

def treetrunk():
    for i in range(2):
        leif.forward(90)
        leif.left(90)
        leif.forward(300)
        leif.left(90)

def tree():
    for i in range(1):
        leif.color("saddle brown")
        leif.begin_fill()
        treetrunk()
        leif.end_fill()
        leif.forward(20)
        leif.left(90)
        leif.forward(300)
        leif.color("forest green")
        leif.begin_fill()
        leif.circle(90)
        leif.right(45)
        leif.forward(20)
        leif.circle(80)
        leif.right(45)
        leif.forward(75)
        leif.circle(70)
        leif.right(200)
        leif.forward(20)
        leif.circle(100)
        leif.right(45)
        leif.forward(90)
        leif.circle(70)
        leif.end_fill()


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
cloud()
fluffy.penup()
fluffy.goto(290,220)
fluffy.pendown()
cloud()
fluffy.penup()
fluffy.goto(-350,-20)
fluffy.penup()
cloud()

shatter.penup()
shatter.goto(-5, -100)
shatter.pendown()
shatter.color("lavender")
shatter.begin_fill()
window()
shatter.penup()
shatter.goto(150,-100)
shatter.pendown()
window()
shatter.end_fill()

leif.penup()
leif.goto(360,-330)
leif.pendown()
tree()


turtle.exitonclick()
