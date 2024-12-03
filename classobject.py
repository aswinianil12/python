class rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l * self.b

    def perimeter(self):
        return 2 * (self.l + self.b)

    def display(self):
        print(f"Area of rectangle: {self.area()}")
        print(f"perimeter of rectangle: {self.perimeter()}")

    def compare_area(self,other):
        if self.area() == other.area():
            print("\nRectangle are equal in area: ")
        elif self.area() > other.area():
            print("\nRectangle 1 is greater than Rectangle 2.")
        else:
            print("\nRectangle 2 is greater than Rectangle 1. ")


print("Enter dimensions of the first rectangle:")
l1 = int(input("Enter length1: "))
b1 = int(input("Enter breadth1"))
rect1=rectangle(l1,b1)
rect1.display()

print("Enter dimensions of the second rectangle:")
l2 = int(input("Enter length2: "))
b2 = int(input("Enter breadth2"))
rect2=rectangle(l2,b2)
rect2.display()


