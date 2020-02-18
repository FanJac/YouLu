import pygame
from pygame.locals import *
from sys import exit
from part_1 import part_1_


# FPS = 200000    # 设置帧率
fpsClock = pygame.time.Clock()
background_image_file_name = 'data/image/background_1.JPG'
option_image_file_name = 'data/image/option_1.JPG'
option_selected_image_file_name = 'data/image/option_1_selected.JPG'


class Menu:

    def __init__(self, screen):
        self.screen = screen
        self.current = 0

    def run(self):

        background = pygame.image.load(background_image_file_name).convert()
        x, y = pygame.mouse.get_pos()
        # 鼠标移至选项框时选项框变色
        if 314 < x < 710 and 300 < y < 354:
            option_1 = pygame.image.load(option_selected_image_file_name).convert()
            option_2 = pygame.image.load(option_image_file_name).convert()
            option_3 = pygame.image.load(option_image_file_name).convert()
        elif 314 < x < 710 and 400 < y < 454:
            option_1 = pygame.image.load(option_image_file_name).convert()
            option_2 = pygame.image.load(option_selected_image_file_name).convert()
            option_3 = pygame.image.load(option_image_file_name).convert()
        elif 314 < x < 710 and 500 < y < 554:
            option_1 = pygame.image.load(option_image_file_name).convert()
            option_2 = pygame.image.load(option_image_file_name).convert()
            option_3 = pygame.image.load(option_selected_image_file_name).convert()
        else:
            option_1 = pygame.image.load(option_image_file_name).convert()
            option_2 = pygame.image.load(option_image_file_name).convert()
            option_3 = pygame.image.load(option_image_file_name).convert()
        # 获取鼠标事件
        for e in pygame.event.get():

            if e.type == QUIT:
                exit()
                return'quit'
            elif e.type == MOUSEBUTTONDOWN:
                x, y = e.pos
                if 314 < x < 710 and 300 < y < 354:
                    return 'part_1'
                elif 314 < x < 710 and 400 < y < 454:
                    print("test222222222222222222222222222222222222")
                elif 314 < x < 710 and 500 < y < 554:
                    print("test333333333333333333333333333333333333")
        self.screen.blit(background, (0, 0))
        self.screen.blit(option_1, (314, 300))
        self.screen.blit(option_2, (314, 400))
        self.screen.blit(option_3, (314, 500))
        pygame.display.update()
        # fpsClock.tick(FPS)
        return 'menu'


def run():

    pygame.init()
    size = width, height = 1079, 720
    screen = pygame.display.set_mode(size, 0, 32)
    m = Menu(screen)
    p = part_1_(screen)

    page = 'menu'
    while True:
        if page == 'menu':
            page = m.run()
            print(m.run())
        elif page == 'part_1':
            page = p.run()
            print(page)
        else:
            exit()


if __name__ == '__main__':
    run()
