# Class and Object

# Class is a blueprint for creating objects
# Object is an instance of a class
# class : Humnan
# object : Jana, Ali, etc.

class Human:
    # All functions inside a class are called methods
    # self is a reference to the current instance of the class
    # All functions in the classes should have at least one parameter, which is self

    # Constructor is a special method that is called when an object is created
    def __init__(self, name, age):
        self.name = name  # this is an instance variable
        self.age = age  # this is an instance variable

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


human = Human("Jana", 22)
# this will return True, because human is an instance of Human class
isinstance(human, Human)
