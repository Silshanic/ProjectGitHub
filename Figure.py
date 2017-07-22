class Figure:
    pass


class Point(Figure):

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle(Point):

    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r


class CTriangle(Circle):

    def __init__(self, x, y, r):
        super().__init__(x, y, r)


class Polygon(Figure):

    def __init__(self, *points):
        self.points = points


class Line(Polygon):

    def __init__(self, p1, p2):
        super().__init__(p1, p2)
        self.p1 = p1
        self.p2 = p2


class Triangle(Polygon):

    def __init__(self, p1, p2, p3):
        super().__init__(p1, p2, p3)
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3


class IsoscelesTriangle(Triangle):

    def __init__(self, p1, p2, l):
        super().__init__(p1, p2, 0)
        self.l = l


class Rectangle(Polygon):

    def __init__(self, l_d, r_u):
        super().__init__(l_d, r_u)
        self.l_d = l_d
        self.r_u = r_u


class Square(Rectangle):

    def __init__(self, p, l):
        super().__init__(p, 0)
        self.p = p
        self.l = l
