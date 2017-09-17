import figures


class Character(figures.Drawable):

    def __init__(self, x, y):
        self.body_parts = {'head': figures.Circle(x + 25, y + 25, 25),
                           'torso': figures.Line(figures.Point(x + 25, y + 50), figures.Point(x + 25, y + 100)),
                           'l_arm': figures.Line(figures.Point(x + 25, y + 50), figures.Point(x, y + 75)),
                           'r_arm': figures.Line(figures.Point(x + 25, y + 50), figures.Point(x + 50, y + 75)),
                           'l_leg': figures.Line(figures.Point(x + 25, y + 100), figures.Point(x, y + 150)),
                           'r_leg': figures.Line(figures.Point(x + 25, y + 100), figures.Point(x + 50, y + 150))}
        self.trigger = 0

    def draw(self, game_display):
        for body_part in self.body_parts.values():
            body_part.draw(game_display)

    def wave_arms(self, game_display):
        if self.body_parts['l_arm'].p2.y == self.body_parts['torso'].p1.y:
            self.trigger = 1
        elif self.body_parts['l_arm'].p2.y == self.body_parts['torso'].p1.y + 25:
            self.trigger = 0
        if self.trigger == 0:
            self.body_parts['l_arm'].p2.y += -1
            self.body_parts['l_arm'].p2.x += -0.314
            self.body_parts['r_arm'].p2.y += -1
            self.body_parts['r_arm'].p2.x += 0.314
        elif self.trigger == 1:
            self.body_parts['l_arm'].p2.y += 1
            self.body_parts['l_arm'].p2.x += 0.314
            self.body_parts['r_arm'].p2.y += 1
            self.body_parts['r_arm'].p2.x += -0.314
        self.draw(game_display)


class Snake(figures.Drawable):

    # Для ограничения скорости
    update_count_max = 8
    update_count = 0

    def __init__(self, length):
        self.length = length
        self.segment = []
        self.step = 20
        self.direction = 1
        for i in range(0, length):
            self.segment.append(figures.Point(340 + i * self.step, 280))

    def update(self):

        self.update_count = self.update_count + 1
        if self.update_count > self.update_count_max:

            for i in range(self.length - 1, 0, -1):
                self.segment[i].x = self.segment[i - 1].x
                self.segment[i].y = self.segment[i - 1].y

            if self.direction == 0:
                self.segment[0].x = self.segment[0].x + self.step
            if self.direction == 1:
                self.segment[0].x = self.segment[0].x - self.step
            if self.direction == 2:
                self.segment[0].y = self.segment[0].y - self.step
            if self.direction == 3:
                self.segment[0].y = self.segment[0].y + self.step

            self.update_count = 0

    def move_right(self):
        if self.direction != 1:
            self.direction = 0

    def move_left(self):
        if self.direction != 0:
            self.direction = 1

    def move_up(self):
        if self.direction != 3:
            self.direction = 2

    def move_down(self):
        if self.direction != 2:
            self.direction = 3

    def draw(self, game_display):
        for i in range(0, self.length):
            figures.Square(self.segment[i], 20).draw(game_display)
