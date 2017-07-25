class Figure:
    pass


class Point(Figure):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point(%s, %s)' % (self.x, self.y)

    def __mul__(self, n):
        return Point(self.x * n, self.y * n)

    def __truediv__(self, n):
        return Point(self.x / n, self.y / n)


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
        self.center = Point((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)

    def __add__(self, v):
        return Line(self.points[0], Point(self.points[0].x + self.points[1].x - self.points[0].x + v.points[1].x - v.points[0].x, self.points[0].y + self.points[1].y - self.points[0].y + v.points[1].y - v.points[0].y))

    def __sub__(self, v):
        return Line(self.points[0], Point(self.points[0].x + self.points[1].x - self.points[0].x - v.points[1].x + v.points[0].x, self.points[0].y + self.points[1].y - self.points[0].y - v.points[1].y + v.points[0].y))

    def __abs__(self):
        return ((self.points[0].x - self.points[1].x)**(2) + (self.points[0].y - self.points[1].y)**(2))**(.5)


class Triangle(Polygon):

    def __init__(self, p1, p2, p3):
        super().__init__(p1, p2, p3)


class IsoscelesTriangle(Triangle):

    def __init__(self, p1, p2, l):
        center = Line(p1, p2).center
        ah = abs(Line(p1, center))
        ch = ((l*l) - (ah * ah))**(.5)
        if p1.x == p2.x:
            p3 = Point(center.x + ch, center.y)
        elif p1.y == p2.y:
            p3 = Point(center.x, center.y + ch)
        else:
            sin = abs((p1.y - p2.y) / 2) / ah
            c = Point(sin * ch, ((ch * ch) - ((sin * ch) ** 2))**(.5))
            if p1.y > p2.y:
                p3 = Point(center.x + c.x, center.y + c.y)
            else:
                p3 = Point(center.x - c.x, center.y + c.y)
        super().__init__(p1, p2, p3)


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

