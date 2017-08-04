from figures import *
import pygame

pygame.init()

display_width = 800
display_height = 600

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
        line = Line(p1, p2)
        line.color = RED
        line.draw(game_display)
        p1.draw(game_display)
        p2.draw(game_display)
        polygon = Polygon(Point(400, 500), Point(700, 550), Point(600, 400))
        polygon.color = CYAN
        polygon.draw(game_display)

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
