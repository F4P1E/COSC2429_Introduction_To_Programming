from math import pi


class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * pi * self.radius


c = Circle(4)
print(c.get_area())
print(c.get_perimeter())
