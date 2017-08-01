import math
import pygame


class Figure:
    pass


class Point(Figure):

    def __init__(self, x, y):
        self.x = round(x)
        self.y = round(y)

    def __repr__(self):
        return '<Point(x={0}, y={1}) figure>'.format(self.x, self.y)

    def __mul__(self, n):
        return Point(self.x * n, self.y * n)

    def __truediv__(self, n):
        return Point(self.x / n, self.y / n)

    def draw(self, game_display):
        pygame.draw.circle(game_display, BLACK, (self.x, self.y), 1)


class Circle(Point):

    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def __repr__(self):
        return '<Circle(x={0}, y={1}, r={2}) figure>'.format(self.x, self.y, self.r)

    def draw(self, game_display):
        pygame.draw.circle(game_display, BLACK, (self.x, self.y), self.r)


class Polygon(Figure):

    def __init__(self, *points):
        self.points = points

    def __repr__(self):
        return '<{0}{1} figure>'.format(self.__class__.__name__, self.points)

    def draw(self, game_display):
        pygame_points = [[point.x, point.y] for point in self.points]
        pygame.draw.polygon(game_display, BLACK, pygame_points)


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

    def draw(self, game_display):
        pygame.draw.line(game_display, BLACK, [self.points[0].x, self.points[0].y], [self.points[1].x, self.points[1].y])


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


class EquilateralPolygon(Polygon):

    def __init__(self, center_point, r, vertices):
        points = []
        angles = 360 / vertices
        for n in range(vertices):
            angle = angles * n
            points.append(Point(center_point.x + math.cos(math.radians(angle)) * r, center_point.y + math.sin(math.radians(angle)) * r))
        super().__init__(*points)


pygame.init()

display_width = 800
display_height = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()


def game_loop():

    game_exit = False

    while not game_exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

        game_display.fill(WHITE)

        p1 = Point(100, 200)
        p2 = Point(200, 300)
        p1.draw(game_display)
        p2.draw(game_display)
        Line(p1, p2).draw(game_display)
        Polygon(Point(400, 500), Point(700, 550), Point(600, 400)).draw(game_display)

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()

