square = lambda s: s*s
rectangle = lambda l,b: l*b
circle = lambda r: 3.14*r*r
s = int(input("Enter length of square: "))
l = int(input("Enter length of rectangle: "))
b = int(input("Enter breadth of rectangle: "))
r = int(input("Enter radius of circle: "))
print("Ares of square is ",square(s))
print("Ares of rectangle is ",rectangle(l,b))
print("Ares of circle is ",circle(r))
