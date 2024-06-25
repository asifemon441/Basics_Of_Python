"""
Class and Objects

-blueprint for creating the objects
-encapsulate data and behavior

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def bark(self):
        print("Woof!")

my_dog = Dog("Buddy",3)
my_dog.bark()
print(my_dog.name)
"""

"""
Access Specifiers
    - controls visibility and accessibility of class members
    -Three access specifiers
        1. public ..... default
        2. protected _
        3. private __
"""
class MyClass: #Base Class
    def __init__(self):
        self.public_member = "Public"
        self._protected_member= "Protected"
        self.__private = "private"
    def get_private_member(self):
        print(self.__private)

class MyDerivedClass(MyClass): #Subclass
    def __init__(self):
        super().__init__()
    def get_protected_member(self):
        return self._protected_member
my_obj = MyClass()
print(my_obj.public_member)
print(my_obj._protected_member)
my_obj.get_private_member()

myder = MyDerivedClass()
print(myder.public_member)
print(myder.get_protected_member())
myder.get_private_member()











