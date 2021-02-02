import graphics.rectangle
l=int(input("Enter length of rectangle :"))
b=int(input("Enter breadth of rectangle :"))
print("Area of rectangle is :",graphics.rectangle.rarea(l,b))
print("Perimeter of rectangle is :",graphics.rectangle.rperimeter(l,b))

from graphics.circle import carea
from graphics.circle import cperimeter
r=int(input("Enter radius of circle :"))
print("Area of circle is :",carea(r))
print("Perimeter of circle is :",cperimeter(r))

from graphics.dgraphics import cuboid as c
l=int(input("Enter length of cuboid :"))
b=int(input("Enter breadth of cuboid :"))
h=int(input("Enter height of cuboid :"))
print("Area of cuboid is :",c.cuarea(l,b,h))
print("Perimeter of rectangle is :",c.cuperimeter(l,b,h))

from graphics.dgraphics.sphere import *
r=int(input("Enter radius of sphere :"))
print("Area of sphere is :",sarea(r))
print("Perimeter of sphere is :",sperimeter(r))
