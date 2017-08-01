from figures import *
import pygame

pygame.init()

display_width = 800
display_height = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PINK = (255, 0, 255)
CYAN = (0, 255, 255)

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
        Line(p1, p2).draw(game_display, GREEN)
        p1.draw(game_display, BLUE)
        p2.draw(game_display, RED)
        Polygon(Point(400, 500), Point(700, 550), Point(600, 400)).draw(game_display, CYAN)

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
