# Define a class Rectangle with length and breadth as instance object variables.
# Provide setDimensions(), showDimensions() and getArea() method in it.

class Rectangle:
    def setDimensions(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def showDimensions(self):
        print(f"Area of a Rectangle whose Length = {self.length} and breadth = {self.breadth} is = ")

    def getArea(self):
        print(self.length * self.breadth)
    
obj = Rectangle ()
obj.setDimensions(4, 5)
obj.showDimensions()
obj.getArea()
