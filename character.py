import figures
import pygame
import time
import colors


class Character(figures.Drawable):

    def __init__(self, x, y):
        self.body_parts = {'head': figures.Circle(x + 25, y + 25, 25),
                           'torso': figures.Line(figures.Point(x + 25, y + 50), figures.Point(x + 25, y + 100)),
                           'l_arm': figures.Line(figures.Point(x + 25, y + 50), figures.Point(x, y + 75)),
                           'r_arm': figures.Line(figures.Point(x + 25, y + 50), figures.Point(x + 50, y + 75)),
                           'l_leg': figures.Line(figures.Point(x + 25, y + 100), figures.Point(x, y + 150)),
                           'r_leg': figures.Line(figures.Point(x + 25, y + 100), figures.Point(x + 50, y + 150))}

    def draw(self, game_display):
        for body_part in self.body_parts.values():
            body_part.draw(game_display)

    def wave_arms(self, game_display):
        l_arm_up = self.body_parts['l_arm'].p1.y
        l_arm_down = self.body_parts['l_arm'].p2.y
        while self.body_parts['l_arm'].p2.y != l_arm_up:
            self.body_parts['l_arm'].color = colors.WHITE
            self.body_parts['r_arm'].color = colors.WHITE
            self.body_parts['l_arm'].draw(game_display)
            self.body_parts['r_arm'].draw(game_display)
            self.body_parts['l_arm'].color = colors.BLACK
            self.body_parts['r_arm'].color = colors.BLACK
            self.body_parts['l_arm'].p2.y += -1
            self.body_parts['l_arm'].p2.x += -0.314
            self.body_parts['r_arm'].p2.y += -1
            self.body_parts['r_arm'].p2.x += 0.314
            self.body_parts['l_arm'].draw(game_display)
            self.body_parts['r_arm'].draw(game_display)
            pygame.display.update()
            time.sleep(0.005)
        while self.body_parts['l_arm'].p2.y != l_arm_down:
            self.body_parts['l_arm'].color = colors.WHITE
            self.body_parts['r_arm'].color = colors.WHITE
            self.body_parts['l_arm'].draw(game_display)
            self.body_parts['r_arm'].draw(game_display)
            self.body_parts['l_arm'].color = colors.BLACK
            self.body_parts['r_arm'].color = colors.BLACK
            self.body_parts['l_arm'].p2.y += 1
            self.body_parts['l_arm'].p2.x += 0.314
            self.body_parts['r_arm'].p2.y += 1
            self.body_parts['r_arm'].p2.x += -0.314
            self.body_parts['l_arm'].draw(game_display)
            self.body_parts['r_arm'].draw(game_display)
            pygame.display.update()
            time.sleep(0.005)
