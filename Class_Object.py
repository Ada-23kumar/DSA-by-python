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

