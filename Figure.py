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
        h_x = (p1.x + p2.x) / 2 # X координата середины
        h_y = (p1.y + p2.y) / 2 # Y координата середины
        ah = ((p1.x - h_x)**(2) + (p1.y - h_y)**(2))**(.5) # Длина половины основания
        ch = ((l*l) - (ah * ah))**(.5) # Длина высоты
        if p1.x == p2.x:
            p3 = Point(h_x + ch, h_y)
        elif p1.y == p2.y:
            p3 = Point(h_x, h_y + ch)
        else:
            sin = abs((p1.y - p2.y) / 2) / ah
            c_x = sin * ch
            c_y = ((ch * ch) - (c_x * c_x))**(.5)
            p3 = Point(h_x + c_x, h_y + c_y)
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

