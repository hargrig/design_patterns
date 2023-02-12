# Decorator pattern allows a user to add new functionality 
# to an existing object without altering its structure.
# This type of design pattern comes under structural 
# pattern as this pattern acts as a wrapper to existing class.
# This pattern creates a decorator class which wraps the original class 
# and provides additional functionality keeping class methods signature intact.
# We are demonstrating the use of decorator pattern via following example 
# in which we will decorate a shape with some color without alter shape class.

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        raise NotImplemented

class Rectangle(Shape):
    def draw(self):
        print("Shape: Rectangle")

class Circle(Shape):
    def draw(self):
        print("Shape: Circle")


class ShapeDecorator(Shape):
    def __init__(self, decorated_shape: Shape):
        self.decorated_shape = decorated_shape

    def draw(self):
        self.decorated_shape.draw()

class RedShapeDecorator(ShapeDecorator):
    def __init__(self, decorated_shape: Shape):
        super().__init__(decorated_shape)

    def draw(self):
        self.decorated_shape.draw()	       
        self.set_red_border()

    def set_red_border(self):
        print("Border Color: Red")


class DemoDecoratorPattern:
    def main(self):
        circle = Circle()
        red_circle = RedShapeDecorator(Circle())
        red_rectangle = RedShapeDecorator(Rectangle())

        print("Circle with normal border")
        circle.draw()
        print("\n")

        print("Circle of red border")
        red_circle.draw()
        print("\n")

        print("Rectangle of red border")
        red_rectangle.draw()
        print("\n")


if __name__ == "__main__":
    demo = DemoDecoratorPattern()
    demo.main()