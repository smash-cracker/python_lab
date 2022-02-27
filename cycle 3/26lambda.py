square = lambda s: s*s
rectangle = lambda l,b: l*b
circle = lambda r: 3.14*r*r
n = int(input("1. Square 2. Circle 3. Rectangle \n Enter choice: "))
if n==1:
    s = int(input("Enter length of square: "))
    print("Ares is ",square(s))
if n==2:
    l = int(input("Enter length of rectangle: "))
    b = int(input("Enter breadth of rectangle: "))
    print("Ares is ",rectangle(l,b))
if n==3:
    r = int(input("Enter radius of circle: "))
    print("Ares is ",circle(r))
