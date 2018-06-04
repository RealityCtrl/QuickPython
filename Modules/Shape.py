"""Shape Module: Contains class Shape, Square and Circle"""
class Shape:
    """Shape class has funtion: move()"""
    def __init__(self,x,y):
        self.x = x
        self.y = y


    def move(self, deltaX, deltaY):
        self.x = self.x + deltaX
        self.y = self.y = deltaY


class Square(Shape):
    """Square Class inherits from shape """
    def __init__(self, side=1, x=0, y=0):
        Shape.__init__(self,x,y)
        self.side = side


class Circle(Shape):
    """Circle Class: inherits from Shape and has methods area and perimeter"""
    from math import pi

    def __init__(self, radius, x=0, y=0):
        Shape.__init__(self, x, y)
        self.radius = radius
        self.a = self.radius * self.radius * self.pi
        self.p = 2 * self.pi * self.radius

    def perimeter(self):
        return self.p

    def area(self):
        return self.a

    def __str__(self):
        return "Circle of radius %s, perimeter %f and area %f at coordinates (%d, %d) " \
               % (self.radius, self.p, self.a, self.x, self.y)