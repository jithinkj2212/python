class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def Area(self):
        area=self.length*self.breadth
        return area

    def Perimeter(self):
        perimeter=2*(self.length+self.breadth)
        return perimeter

length1=int(input("Enter the length of the first rectangle:"))
breadth1=int(input("Enter the breadth of the first rectangle:"))

rect1=Rectangle(length1,breadth1)

length2=int(input("Enter the length of the second rectangle:"))
breadth2=int(input("Enter the breadth of the second rectangle:"))

rect2=Rectangle(length2,breadth2)

area1=rect1.Area()
perimeter1=rect1.Perimeter()
area2=rect2.Area()
perimeter2=rect2.Perimeter()

print("\nArea of first rectangle",area1)
print("Area of second rectangle",area2)
print("\nPerimeter of first rectangle",perimeter1)
print("Perimeter of second rectangle",perimeter2)
if rect1.Area() > rect2.Area():
 print("First rectangle have more area:",area1)
else:
 print("second rectangle have more area:",area2)
        
