from graphics import circle
from graphics import rectangle
from graphics.subg import cuboid
from graphics.subg import sphere
a = circle.area(4)
b = rectangle.area(3,4)
c = cuboid.area(3,4,5)
d = sphere.area(4)
print("Area of circle is ",circle.area(4))
print("perimeter of circle is ",circle.perimeter(4))
print("Area of rectangle is ",rectangle.area(4,5))
print("perimeter of rectangle is ",rectangle.perimeter(4,5))
print("Area of cuboid is ",cuboid.area(4,5,6))
print("perimeter of cuboid is ",cuboid.perimeter(4,5,6))
print("Area of sphere is ",sphere.area(4))
print("perimeter of sphere is ",sphere.perimeter(4))
