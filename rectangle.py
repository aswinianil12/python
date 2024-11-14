class Rectangle:
    def __init__(self, length, breadth):
        # Initialize the length and breadth of the rectangle
        self.length = length
        self.breadth = breadth

    def area(self):
        # Calculate the area of the rectangle
        return self.length * self.breadth

# Example of creating a rectangle and finding the area
length = int(input("Enter the length : "))
breadth = int(input("Enter the breadth: "))
rect = Rectangle(length,breadth)
print("Area of the rectangle:", rect.area())
