import math
from pygame import draw

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PINK = (255, 0, 255)
CYAN = (0, 255, 255)
SKIN = (250, 189, 183)


class Figure:

    def __init__(self, color):
        self.color = color

    def draw(self, game_display):
        raise NotImplementedError


class Point(Figure):

    def __init__(self, x, y, color=BLACK):
        self.x = round(x)
        self.y = round(y)
        super().__init__(color)

    def __repr__(self):
        return '<Point(x={0}, y={1}) figure>'.format(self.x, self.y)

    def __mul__(self, n):
        return Point(self.x * n, self.y * n)

    def __truediv__(self, n):
        return Point(self.x / n, self.y / n)

    def __eq__(self, p):
        return self.x == p.x and self.y == p.y

    def draw(self, game_display):
        draw.circle(game_display, self.color, (self.x, self.y), 1)


class Circle(Point):

    def __init__(self, x, y, r, color=BLACK):
        self.r = round(r)
        if self.r <= 0:
            raise ValueError('Radius must be 1 or higher')
        super().__init__(x, y, color)

    def __repr__(self):
        return '<Circle(x={0}, y={1}, r={2}) figure>'.format(self.x, self.y, self.r)

    def draw(self, game_display):
        draw.circle(game_display, self.color, (self.x, self.y), self.r)


class Polygon(Figure):

    def __init__(self, *points, color=BLACK):
        if len(points) < 3:
            raise ValueError('Polygon must have 3 or more vertices')
        self.points = points
        super().__init__(color)

    def __repr__(self):
        return '<{0}{1} figure>'.format(self.__class__.__name__, self.points)

    def draw(self, game_display):
        pygame_points = [[point.x, point.y] for point in self.points]
        draw.polygon(game_display, self.color, pygame_points)


class Line(Figure):

    def __init__(self, p1, p2, color=BLACK):
        self.p1 = p1
        self.p2 = p2
        self.center = Point((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)
        super().__init__(color=color)

    def __add__(self, v):
        return Line(self.p1, Point(self.p2.x + v.p2.x - v.p1.x, self.p2.y + v.p2.y - v.p1.y))

    def __sub__(self, v):
        return Line(self.p1, Point(self.p2.x - v.p2.x + v.p1.x, self.p2.y - v.p2.y + v.p1.y))

    def __abs__(self):
        return ((self.p1.x - self.p2.x)**2 + (self.p1.y - self.p2.y)**2)**.5

    def __eq__(self, l):
        return self.p1 == l.p1 and self.p2 == l.p2

    def draw(self, game_display):
        draw.line(game_display, self.color, [self.p1.x, self.p1.y], [self.p2.x, self.p2.y])


class Triangle(Polygon):

    def __init__(self, p1, p2, p3, color=BLACK):
        if (p2.y-p1.y)/abs(Line(p2, p1)) == (p3.y-p2.y)/abs(Line(p3, p2)):
            raise ValueError('Points must not be on the same line')
        super().__init__(p1, p2, p3, color=color)


class IsoscelesTriangle(Triangle):

    def __init__(self, p1, p2, l, color=BLACK):
        center = Line(p1, p2).center
        ah = abs(Line(p1, center))
        if l <= ah:
            raise ValueError('Side length must be bigger than base length')
        ch = ((l*l) - (ah * ah))**.5
        if p1.x == p2.x:
            p3 = Point(center.x + ch, center.y)
        elif p1.y == p2.y:
            p3 = Point(center.x, center.y + ch)
        else:
            sin = abs((p1.y - p2.y) / 2) / ah
            c = Point(sin * ch, ((ch * ch) - ((sin * ch) ** 2))**.5)
            if p1.y > p2.y:
                p3 = Point(center.x + c.x, center.y + c.y)
            else:
                p3 = Point(center.x - c.x, center.y + c.y)
        super().__init__(p1, p2, p3, color=color)


class Rectangle(Polygon):

    def __init__(self, l_d, r_u, color=BLACK):
        l_u = Point(l_d.x, r_u.y)
        r_d = Point(r_u.x, l_d.y)
        super().__init__(l_d, l_u, r_u, r_d, color=color)


class Square(Rectangle):

    def __init__(self, p, l, color=BLACK):
        l_d = p
        r_u = Point(p.x + l, p.y + l)
        super().__init__(l_d, r_u, color=color)


class EquilateralPolygon(Polygon):

    def __init__(self, center_point, r, vertices, color=BLACK):
        if r <= 0:
            raise ValueError('Radius must be 1 or higher')
        if vertices < 3:
            raise ValueError('Polygon must have 3 or more vertices')
        points = []
        angles = 360 / vertices
        for n in range(vertices):
            angle = angles * n
            points.append(Point(center_point.x + math.cos(math.radians(angle)) * r,
                                center_point.y + math.sin(math.radians(angle)) * r))
        super().__init__(*points, color=color)
