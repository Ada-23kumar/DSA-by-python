# Define a python class Person with instance object variables name and age. Set
# Instance object variables in __init__() method. Also define show() method to display
# name and age of a person.
class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"My name is {self.name}and my age is {self.age}")

obj = Person("Adarsh", 19)
obj.show()

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def show(self):
#         print(f"my name is {self.name} and my age {self.age}")
        
# obj=Person("abhay",23)
# obj.show() 

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
