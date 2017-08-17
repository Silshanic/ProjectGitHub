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
