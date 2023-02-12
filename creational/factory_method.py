# Factory pattern is one of the most used design pattern. 
# This type of design pattern comes under creational pattern 
# as this pattern provides one of the best ways to create an object.
# In Factory pattern, we create object without exposing the creation 
# logic to the client and refer to newly 
# created object using a common interface.

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw():
        raise NotImplemented


class Rectangle(Shape):
    def draw(self):
        print("I'm a Rectangle")

class Square(Shape):
    def draw(self):
        print("I'm a Square")

class Circle(Shape):
    def draw(self):
        print("I'm a Circle")


class ShapeFactory:
    def get_shape(self, type: str = None) -> Shape:
        if type.lower() == "circle":
            return Circle()
        elif type.lower() == "rectangle":
            return Rectangle()
        elif type.lower() == "square":
            return Square()
        else:
            return None


class DemoFactoryPattern:
    def main(self):
        shape_factory = ShapeFactory()

        shape1 = shape_factory.get_shape("CIRCLE")
        shape1.draw()

        shape2 = shape_factory.get_shape("RECTANGLE")
        shape2.draw()

        shape3 = shape_factory.get_shape("SQUARE")
        shape3.draw()


if __name__ == "__main__":
    demo = DemoFactoryPattern()
    demo.main()
