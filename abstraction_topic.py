from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def calculate_area(self):
        return 3.14* self.radius*self.radius
radius = 5
my_cricle = Circle(radius)
area = my_cricle.calculate_area()
print(f"Area of Circle with Radius as {radius} is {area}")

