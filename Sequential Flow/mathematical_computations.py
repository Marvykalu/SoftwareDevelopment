import math

""" This program computes the area of a trapezium with given datum:
senior base = a, minor base = b, and height = h respectively
"""
a, b, h = 8.4, 4, 7.2 #assigning values to our variables
Area = (a + b)/2 * h #formula
print('The area of a trapezium with senior base 8.4, minor base 4 and height 7.2 is', Area)

#--------------------------------------
""" This program computes the length of circumference and the area of a circle, given a
with the radius of the circle given by the user
"""
r = int(input("Enter a value for radius of the circle: "))
length, area = 2 * math.pi * r, math.pi * r**2 #formula
print("Given r=", r, "the length of circumference and area of the circle are {} and {} respectively".format(round(length,2), round(area,2)))


#---------------------------------------
""" This program computes the volume of a cone with given height h and radius r
"""
h, r = 5, 1.5 #assigning values to our variables
Volume = (math.pi * r**2 * h)/3 #formula
print("The volume of the cone is", Volume)

#--------------------------------------
"""
This program converts Fahrenheit degrees F to Celcius degrees C
"""
F = int(input("Enter a temperature in Farenheit: "))
C = (F - 32)*(5/9)
print(str(F)+"Fahrenheit =", str(round(C))+"Celcius")

#-----------------------------------
"""This program computes the value of a complex expression 
"""
x = int(input("Enter value for x: "))
y = int(input("Enter value for y: "))

a = x**(2+y)
b = (1/x ) + math.sin(math.radians(y)) 
num = math.sqrt(a)
denom = b * 2

expression = num/denom
print("The value of the complex expression is:", expression)

#------------------------------------
"""This program computes the value of a bell-shaped Gaussian function
"""
x = 1
m = 0
s = 2

p = (x - m)**2 / 2* s**2
a = s * math.sqrt(2 * math.pi)
Gaussian = 1/a * math.exp(- p)
print("The value of the bell-shaped Gaussian function is: ", Gaussian)

#====================================
"""This program computes the coefficients (slope a and intercept b) in the equation of a staright line y = ax + b
through two points (x0,y0) and (x1,y1) given by the user 
"""
y0 = int(input("Enter the first y point: "))
y1 = int(input("Enter the second y point: "))
x0 = int(input("Enter the first x point: "))
x1 = int(input("Enter the second x point: "))

a = (y1 - y0)/(x1-x0)
b = y0 - a*x0
print("The slope and intercept of the straight line are respectively {} and {}".format(a, b))


