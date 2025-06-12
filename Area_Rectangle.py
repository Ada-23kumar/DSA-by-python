# Define a class Rectangle with length and breadth as instance object variables.
# Provide setDimensions(), showDimensions() and getArea() method in it.

class Rectangle:
    def __init__(self):
        print("The area of a Rectangle")
        self.length = int(input("Enter the length: "))
        self.breadth= int(input("Enter the breadth: "))
    # def setDimensions(self):
    #     self.length 
    #     self.breadth
    def showDimensions(self):
        print(f"Area of a Rectangle whose Length = {self.length} and breadth = {self.breadth} is = ")

    def getArea(self):
        print(self.length * self.breadth)


if __name__ == "__main__":
    
    obj = Rectangle ()
    # obj.setDimensions(4, 5)
    obj.showDimensions()
    obj.getArea()
