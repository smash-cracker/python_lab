class Rectangle:
    def __init__(self,length,breadth) :
        self.length = length
        self.breadth = breadth
    def area(self):
        area = self.length*self.breadth
        return area
    def perimeter(self):
        perimeter = 2*(self.length*self.breadth)
        return perimeter
        
a=int(input("Enter length of rectangle: "))
b=int(input("Enter breadth of rectangle: "))
rect = Rectangle(a,b)
print(rect.area())
print(rect.perimeter())