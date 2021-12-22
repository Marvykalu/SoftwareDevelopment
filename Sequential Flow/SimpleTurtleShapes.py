import turtle
import math
from turtle import *

#=======================equilateral triangle
"""This program draws an equilateral triangle of length 100
"""
turtle.speed("slow")
for i in range(3):
    turtle.forward(100)
    turtle.left(120)



#========================rectangle
"""This program draws an rectangle
"""
turtle.speed('slow')
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
#turtle.up()
turtle.forward(100)
turtle.right(90)
#turtle.down()
turtle.forward(50)

#======================simple house

turtle.speed("slow")
turtle.forward(100)
turtle.left(90)
turtle.forward(30)
turtle.left(45)
turtle.forward(70)
turtle.left(90)
turtle.forward(70)
turtle.left(45)
turtle.forward(30)
turtle.up()
turtle.left(180)
turtle.forward(30)
turtle.right(90)
turtle.down()
turtle.forward(100)


#======================= isosceles trapezium

a = float(input("Enter the length of side a "))
b = float(input("Enter the length of side b "))
c = float(input("Enter the length of side c "))

turtle.left(60)
turtle.forward(c)
turtle.right(60)
turtle.forward(a)
turtle.right(60)
turtle.forward(c)
turtle.right(120)
turtle.forward(b)

#==================================
"""This program draws an arc on the left of turtle going forward, with
radius r and central angle a provided by user.
"""
r = float(input("Please enter the radius of the arc"))
a = float(input("Please enter value for central angle in radians"))
turtle.color('black', 'black') #color the arc black
begin_fill()
turtle.circle(r, math.degrees(a))
end_fill()
penup()
home()
pendown()

#=====================================
"""This program draws a shape with size given by user.
The shape has equal sides and the angles on each side are equal and sum to 360 degrees and

For example: a square has 4 equal sides as with 90 degrees angle on each side
A rectangle does not have equal sides so the program wont work.
An equilateral traingle has equal sides but the total internal angle does not sum to 360
"""

n = int(input("How many sides does the shape you want have? "))
l = float(input("What is the length of each side "))
pensize(3)

for i in range(n):
    turtle.forward(l)
    turtle.left(360/n)

#==================================
""" This program draws a circular design
"""
for i in range (8):
    turtle.circle(80/(i+1), 360)
    turtle.circle(-80/(i+1),360)
