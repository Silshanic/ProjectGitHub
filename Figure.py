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


class Triangle(Polygon):

    def __init__(self, p1, p2, p3):
        super().__init__(p1, p2, p3)


class IsoscelesTriangle(Triangle):

    def __init__(self, p1, p2, l):
        super().__init__(p1, p2, 0)


class Rectangle(Polygon):

    def __init__(self, l_d, r_u):
        l_u = Point(l_d.x, r_u.y)
        r_d = Point(r_u.x, l_d.y)
        super().__init__(l_d, l_u, r_u, r_d)


class Square(Rectangle):

    def __init__(self, p, l):
        l_d = p
        r_u = Point(p.x + l, p.y + l)
        super().__init__(l_d, r_u)
