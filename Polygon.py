from homeWork.lab1.lab1.Point import Point
from math import tan, fabs
from homeWork.lab1.lab1.annotation import *


class Polygon(Point):
    """ x, y - top of polygon

    """

    def __init__(self, x, y, n, a):
        super().__init__(x, y)
        self.__n = n
        self.__a = a

    def calculate_square(self):
        return self.__n * self.__a**2 / 4.0 * fabs(tan(180/float(self.__n)))


    def get_n(self):
        return self.__n

    @check_values
    def set_n(self, n):
        self.__n = n

    def get_a(self):
        return self.__a

    @check_values
    def set_a(self, a):
        self.__a = a
        print(self.__a)

    def __str__(self):
        return "Square of polygon is " + str(self.calculate_square())

def main():
    polygon = Polygon(10, 20, 6, 20)
    polygon.set_a(40)
    print(polygon.get_a())

if __name__ == '__main__':
    main()