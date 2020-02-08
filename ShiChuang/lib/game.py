import menu
import pygame
from pygame.locals import *
from sys import exit
import menu


background_image_file_name = 'data/image/background_1.JPG'
option_image_file_name = 'data/image/option_1.JPG'


class Menu:

    def __init__(self, screen):
        self.screen = screen
        self.current = 0

    def run(self):
        self.myrect_1 = pygame.Rect(250, 750, 750, 350)
        background = pygame.image.load(background_image_file_name).convert()
        option_1 = pygame.image.load(option_image_file_name).convert()
        # self.opt_size = opt_width, opt_height = 396, 54
        # self.option = pygame.display.set_mode(self.opt_size, 0, 32)
        for e in pygame.event.get():
            if e.type == QUIT:
                exit()
                return'quit'
            elif e.type == KEYDOWN:
                if e.key == K_UP:
                    self.current = (self.current - 1) % len(self.OPTS)
                elif e.key == K_DOWN:
                    self.current = (self.current - 1) % len(self.OPTS)
                elif e.key == K_RETURN:
                    return self.OPTS[self.current].lower()
        self.screen.blit(background, (0, 0))
        self.screen.blit(option_1, (314, 300))
        self.screen.blit(option_1, (314, 400))
        self.screen.blit(option_1, (314, 500))
        return 'menu'


def run():

    pygame.init()
    size = width, height = 1079, 720
    screen = pygame.display.set_mode(size, 0, 32)
    m = Menu(screen)
    while True:

        print(m.run())
        pygame.display.update()


if __name__ == '__main__':
    run()
