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

    @pytest.mark.parametrize('x,y,x_exc,y_exc', [
        (1, 1, 1, 1),
        (1.5, 1.5, 2, 2),
        (0.3, 2.5, 0, 2),  # 1.5 -> 2; 2.5 -> 2. Банковское округление
        (0.99999999, 5, 1, 5)
    ])
    def test_point_rounding(self, x, y, x_exc, y_exc):
        point = figures.Point(x, y)
        # x_exc - excepted x - ожидаемый x; то же и с y
        assert (point.x, point.y) == (x_exc, y_exc)

    @pytest.mark.parametrize('point,num,point_exc', [
        (figures.Point(1, 1), 10, figures.Point(0, 0))
    ])
    def test_point_diving(self, point, num, point_exc):
        div = point / num
        assert div == point_exc

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

    @pytest.mark.parametrize('p1,p2,l,p3', [
        (figures.Point(0, 0), figures.Point(6, 0), 5, figures.Point(3, 4)),
        (figures.Point(0, 0), figures.Point(0, 6), 5, figures.Point(4, 3)),
        (figures.Point(1, 0), figures.Point(7, 4), 5, figures.Point(2, 5))
    ])
    def test_isoscelestriangle_point3(self, p1, p2, l, p3):
        assert figures.IsoscelesTriangle(p1, p2, l).points[2] == p3
