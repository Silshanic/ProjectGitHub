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
        (0.3, 2.5, 0, 2), # 1.5 -> 2; 2.5 -> 2. Банковское округление
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
