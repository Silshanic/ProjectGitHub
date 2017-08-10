import figures
import pytest


class TestFigures:
    def test_base_figure(self):
        with pytest.raises(NotImplementedError):  # проверяем, что draw у
            # Figure возбуждает исключение
            figures.Figure(None).draw(figures.BLACK)

    # pytest.mark.parametrize позволяет вызвать тестовую функцию, перебирая
    # значение аргументов. Перебираем цвета, смотрим, что они устанавливаются
    # правильно
    @pytest.mark.parametrize('color', [
        figures.BLACK, figures.CYAN, figures.RED, figures.GREEN,
    ])
    def test_base_figure_default_color(self, color):
        base_figure = figures.Figure(color)
        assert base_figure.color == color  # проверяем, что цвет установиля
        # верно

    @pytest.mark.parametrize('x,y,x_exp,y_exp', [
        (1, 1, 1, 1),
        (1.5, 1.5, 2, 2),
        (0.3, 2.5, 0, 2),  # 1.5 -> 2; 2.5 -> 2. Банковское округление
        (0.99999999, 5, 1, 5)
    ])
    def test_point_rounding(self, x, y, x_exp, y_exp):
        point = figures.Point(x, y)
        # x_exp - expected x - ожидаемый x; то же и с y
        assert (point.x, point.y) == (x_exp, y_exp)

    @pytest.mark.parametrize('point,num,point_exp', [
        (figures.Point(1, 1), 10, figures.Point(10, 10))
    ])
    def test_point_multiply(self, point, num, point_exp):
        mul = point * num
        assert mul == point_exp

    @pytest.mark.parametrize('point,num,point_exp', [
        (figures.Point(1, 1), 10, figures.Point(0, 0))
    ])
    def test_point_diving(self, point, num, point_exp):
        div = point / num
        assert div == point_exp

    @pytest.mark.parametrize('point,num', [
        (figures.Point(1, 1), 0)
    ])
    def test_point_div_by_zero(self, point, num):
        with pytest.raises(ZeroDivisionError):
            point / num

    @pytest.mark.parametrize('x,y,r,exp_x,exp_y,exp_r', [
        (1, 1, 1, 1, 1, 1),
        (1.5, 1.5, 1.5, 2, 2, 2),
        (0.3, 2.5, 4.5, 0, 2, 4)
    ])
    def test_circle_rounding(self, x, y, r, exp_x, exp_y, exp_r):
        circle = figures.Circle(x, y, r)
        assert (circle.x, circle.y, circle.r) == (exp_x, exp_y, exp_r)

    @pytest.mark.parametrize('x,y,r', [
        (1, 1, 0.5)
    ])
    def test_circle_radius(self, x, y, r):
        with pytest.raises(ValueError):
            figures.Circle(x, y, r)

    @pytest.mark.parametrize('p1,p2,p3,p4', [
        (figures.Point(0, 0), figures.Point(1, 1), figures.Point(2, 1), figures.Point(2, 0))
    ])
    def test_polygon_points(self, p1, p2, p3, p4):
        polygon = figures.Polygon(p1, p2, p3, p4)
        assert polygon.points[0] == p1 and polygon.points[1] == p2 and polygon.points[2] == p3 and \
            polygon.points[3] == p4

    @pytest.mark.parametrize('p1,p2', [
        (figures.Point(1, 1), figures.Point(2, 3))
    ])
    def test_polygon_vertices(self, p1, p2):
        with pytest.raises(ValueError):
            figures.Polygon(p1, p2)

    @pytest.mark.parametrize('line,center', [
        (figures.Line(figures.Point(1, 0), figures.Point(7, 4)), figures.Point(4, 2))
    ])
    def test_line_center(self, line, center):
        assert line.center == center

    @pytest.mark.parametrize('line_1,line_2,line_3', [
        (figures.Line(figures.Point(1, 1), figures.Point(2, 2)),
         figures.Line(figures.Point(2, 2), figures.Point(4, 2)),
         figures.Line(figures.Point(1, 1), figures.Point(4, 2))),
        (figures.Line(figures.Point(1, 1), figures.Point(2, 2)),
         figures.Line(figures.Point(2, 3), figures.Point(3, 5)),
         figures.Line(figures.Point(1, 1), figures.Point(3, 4))),
        (figures.Line(figures.Point(1, 1), figures.Point(2, 2)),
         figures.Line(figures.Point(0, 0), figures.Point(0, 0)),
         figures.Line(figures.Point(1, 1), figures.Point(2, 2)))
    ])
    def test_add_line(self, line_1, line_2, line_3):
        assert (line_1 + line_2) == line_3

    @pytest.mark.parametrize('line_1,line_2,line_3', [
        (figures.Line(figures.Point(1, 1), figures.Point(2, 2)),
         figures.Line(figures.Point(2, 2), figures.Point(4, 2)),
         figures.Line(figures.Point(1, 1), figures.Point(0, 2))),
        (figures.Line(figures.Point(1, 1), figures.Point(2, 2)),
         figures.Line(figures.Point(2, 3), figures.Point(3, 5)),
         figures.Line(figures.Point(1, 1), figures.Point(1, 0))),
        (figures.Line(figures.Point(1, 1), figures.Point(2, 2)),
         figures.Line(figures.Point(0, 0), figures.Point(0, 0)),
         figures.Line(figures.Point(1, 1), figures.Point(2, 2)))
    ])
    def test_sub_line(self, line_1, line_2, line_3):
        assert (line_1 - line_2) == line_3

    @pytest.mark.parametrize('p1,p2,p3', [
        (figures.Point(4, 0), figures.Point(6, 1), figures.Point(5, 3))
    ])
    def test_triangle_points(self, p1, p2, p3):
        triangle = figures.Triangle(p1, p2, p3)
        assert triangle.points[0] == p1 and triangle.points[1] == p2 and triangle.points[2] == p3

    @pytest.mark.parametrize('p1,p2,p3', [
        (figures.Point(0, 0), figures.Point(2, 0), figures.Point(4, 0)),
        (figures.Point(0, 0), figures.Point(0, 2), figures.Point(0, 4)),
        (figures.Point(1, 2), figures.Point(2, 4), figures.Point(4, 8))
    ])
    def test_triangle_error(self, p1, p2, p3):
        with pytest.raises(ValueError):
            figures.Triangle(p1, p2, p3)

    @pytest.mark.parametrize('p1,p2,l,p3', [
        (figures.Point(0, 0), figures.Point(6, 0), 5, figures.Point(3, 4)),
        (figures.Point(0, 0), figures.Point(0, 6), 5, figures.Point(4, 3)),
        (figures.Point(1, 0), figures.Point(7, 4), 5, figures.Point(2, 5))
    ])
    def test_isosceles_triangle_point3(self, p1, p2, l, p3):
        assert figures.IsoscelesTriangle(p1, p2, l).points[2] == p3

    @pytest.mark.parametrize('p1,p2,l', [
        (figures.Point(0, 0), figures.Point(6, 0), 3)
    ])
    def test_isosceles_triangle_length_error(self, p1, p2, l):
        with pytest.raises(ValueError):
            figures.IsoscelesTriangle(p1, p2, l)

    @pytest.mark.parametrize('l_d,r_u,exp_points', [
        (figures.Point(0, 0), figures.Point(4, 2),
         (figures.Point(0, 0), figures.Point(0, 2), figures.Point(4, 2), figures.Point(4, 0)))
    ])
    def test_rectangle_points(self, l_d, r_u, exp_points):
        rectangle = figures.Rectangle(l_d, r_u)
        assert rectangle.points == exp_points

    @pytest.mark.parametrize('point,length,exp_points', [
        (figures.Point(0, 0), 5,
         (figures.Point(0, 0), figures.Point(0, 5), figures.Point(5, 5), figures.Point(5, 0)))
    ])
    def test_square_points(self, point, length, exp_points):
        square = figures.Square(point, length)
        assert square.points == exp_points

    @pytest.mark.parametrize('center_point,radius,vertices,exp_points', [
        (figures.Point(0, 0), 1, 4,
         (figures.Point(1, 0), figures.Point(0, 1), figures.Point(-1, 0), figures.Point(0, -1)))
    ])
    def test_equilateral_polygon_points(self, center_point, radius, vertices, exp_points):
        eq_polygon = figures.EquilateralPolygon(center_point, radius, vertices)
        assert eq_polygon.points == exp_points

    @pytest.mark.parametrize('center_point,radius,vertices', [
        (figures.Point(0, 0), 1, 1),
        (figures.Point(1, 1), 0, 4)
    ])
    def test_equilateral_polygon_error(self, center_point, radius, vertices):
        with pytest.raises(ValueError):
            figures.EquilateralPolygon(center_point, radius, vertices)
