import menu
import pygame
import  sys


def run():
    pygame.init()
    size = width, height = 640, 480
    screen = pygame.display.set_mode(size, 0, 32)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    pygame.quit()


if __name__ == '__main__':
    run()
