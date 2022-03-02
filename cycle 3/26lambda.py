square = lambda s: s*s
rectangle = lambda l,b: l*b
circle = lambda h,bt: 0.5*h*bt 
s = int(input("Enter length of square: "))
l = int(input("Enter length of rectangle: "))
b = int(input("Enter breadth of rectangle: "))
h = int(input("Enter height of triangle: "))
bt = int(input("Enter base of triangle: "))
print("Ares of square is ",square(s))
print("Ares of rectangle is ",rectangle(l,b))
print("Ares of circle is ",circle(h,bt))
