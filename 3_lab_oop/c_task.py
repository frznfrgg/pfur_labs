import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract shape class"""

    @abstractmethod
    def area(self):
        """Calculates area of a figure"""
        pass

    @abstractmethod
    def perimeter(self):
        """calculates a perimeter of a figure"""
        pass


class Rectangle(Shape):
    """Simple rectangle class"""

    def __init__(self, width: float, height: float):
        """Initializes rectangle class

        Args:
            width (float): width of rectangle
            height (float): height of rectangle
        """
        self.width = width
        self.height = height

    def area(self) -> float:
        """Calculates area of a rectangle

        Returns:
            float: area
        """
        return self.width * self.height

    def perimeter(self) -> float:
        """Calculates perimeter of a rectangle

        Returns:
            float: perimeter
        """
        return (self.width + self.height) * 2


class Circle(Shape):
    """Simple circle class"""

    def __init__(self, radius: float):
        """Initializes circle class

        Args:
            radius (float): circles radius
        """
        self.radius = radius

    def area(self) -> float:
        """Calculates area of a circle

        Returns:
            float: area
        """
        return math.pi * self.radius**2

    def perimeter(self) -> float:
        """Calculates perimeter of a circle

        Returns:
            float: perimeter
        """
        return 2 * math.pi * self.radius


class Triangle(Shape):
    """Simple triangle class"""

    def __init__(self, a: float, b: float, c: float):
        """Initializes a simple triangle class

        Args:
            a (float): first side
            b (float): second side
            c (float): third side
        """
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        """Calculates area of a triangle using Gerone formula

        Returns:
            float: area
        """
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self) -> float:
        """Calculates perimeter of a trianngle

        Returns:
            float: perimeter
        """
        return self.a + self.b + self.c


def print_shape_info(shape: Shape):
    """Prints figure info

    Args:
        shape (Shape): a figure to describe
    """
    print(f"Тип фигуры: {type(shape).__name__}")
    print(f"Площадь: {shape.area():.2f}")
    print(f"Периметр: {shape.perimeter():.2f}")
    print()
