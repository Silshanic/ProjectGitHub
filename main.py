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

        p1 = Point(100, 200, CYAN)
        p2 = Point(200, 300, BLUE)
        Line(p1, p2, color=GREEN).draw(game_display)
        p1.draw(game_display)
        p2.draw(game_display)
        Polygon(Point(400, 500), Point(700, 550), Point(600, 400)).draw(game_display)
        Circle(500, 200, 50, RED).draw(game_display)
        Rectangle(Point(0, 0), Point(50, 100), color=BLUE).draw(game_display)
        Triangle(Point(400, 0), Point(500, 0), Point(450, 100), color=CYAN).draw(game_display)
        EquilateralPolygon(Point(100, 450), 50, 7, color=PINK).draw(game_display)
        Square(Point(150, 150), 50, color=YELLOW).draw(game_display)
        IsoscelesTriangle(Point(350, 400), Point(400, 400), 70, color=GREEN).draw(game_display)

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
