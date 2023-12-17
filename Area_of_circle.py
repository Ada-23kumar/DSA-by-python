# Define a class Circle with instance object variable radius. Provide setter and getter
# for radius. Also define getArea() and getCircumference() methods.
class Circle:
    def setRadius(self,radius):
        self.radius = radius
    def getRadius(self):
        return self.radius
    def getCircumference(self):
        print("Circumference",2*22/7*self.getRadius())
    def getArea(self):
        print("Area",22/7*self.getRadius()*self.getRadius())
obj = Circle()
obj.setRadius(5)
obj.getCircumference()
obj.getArea()