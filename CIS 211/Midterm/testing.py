from typing import List
import math


class Shape:
    def __init__(self):
        raise NotImplementedError('Shape cannot be instantiated')

    def area(self):
        raise NotImplementedError('area() is not implemented')

    def __str__(self):
        raise NotImplementedError('__str__() is not implemented')

    def __lt__(self, other: 'Shape') -> bool:
        return self.area() < other.area()


class Circle(Shape):
    def __init__(self, radius: float):
        self._radius = radius

    def area(self):
        return self._radius * self._radius * math.pi

    def __str__(self):
        return f'Circle: radius {self._radius} with area {self.area():.2f}'


class Point(Circle):
    def __init__(self):
        super().__init__(1e-15)  # 1e-15 is a very tiny number

    def __str__(self):
        return 'Point'


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height

    def area(self) -> float:
        return self._width * self._height

    def __str__(self):
        return f'Rectangle: width={self._width}, height={self._height}, area {self.area():.2f}'


def print_shapes(shapes: List[Shape]) -> None:
    for shape in shapes:
        print(shape)


if __name__ == '__main__':
    pt = Point()
    circle1 = Circle(1)
    circle2 = Circle(10)
    rectangle = Rectangle(10, 20)
    print_shapes([pt, circle1, circle2, rectangle])
    print(pt < circle1)
    print(circle1 < circle2)
    print(circle1 < rectangle)
    print(circle2 < rectangle)
