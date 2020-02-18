import pygame
from pygame.locals import *
from sys import exit

# TEST = 1
POINT = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# 存储点的坐标及在数组中的偏移量

POINT[1] = (0, 450, 300)
POINT[2] = (1, 800, 250)
POINT[3] = (2, 900, 400)
POINT[4] = (3, 950, 220)
POINT[5] = (4, 900, 50)
POINT[6] = (5, 200, 600)
POINT[7] = (6, 250, 400)
POINT[8] = (7, 260, 200)
POINT[9] = (8, 100, 100)
POINT[10] = (9, 50, 300)
# myfont = pygame.font.Font(None, 70)
background_image_file_name = 'data/image/background_2.JPG'
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GOLD = (238, 221, 130)
# textImage = myfont.render("START", True, WHITE)
Points = [[2, 1, 0, 0, 0, 0, 1, 1, 0, 0],
          [1, 2, 1, 1, 1, 0, 0, 0, 0, 0],
          [0, 1, 2, 1, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 2, 1, 0, 0, 0, 0, 0],
          [0, 1, 0, 1, 2, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 2, 1, 0, 0, 0],
          [1, 0, 0, 0, 0, 1, 2, 1, 0, 1],
          [1, 0, 0, 0, 0, 0, 1, 2, 1, 0],
          [0, 0, 0, 0, 0, 0, 0, 1, 2, 1],
          [0, 0, 0, 0, 0, 0, 1, 0, 1, 2]]    # 初始化邻接矩阵


class part_1_:

    def __init__(self, screen):
        self.screen = screen
        self.current = 0

    def run(self):
        background = pygame.image.load(background_image_file_name).convert()
        self.screen.blit(background, (0, 0))
        for event in pygame.event.get():

            if event.type == QUIT:
                exit()
        # print(TEST)
        for i in range(2, 11):
            for j in range(1, i):
                if Points[i-1][j-1] == 1:
                    pygame.draw.line(self.screen, WHITE, (POINT[i][1], POINT[i][2]), (POINT[j][1], POINT[j][2]), 5)
        for i in range(1, 11):
            if i == 1:
                pygame.draw.circle(self.screen, RED, (POINT[i][1], POINT[i][2]), 10, 10)
            else:
                pygame.draw.circle(self.screen, GOLD, (POINT[i][1], POINT[i][2]), 10, 10)
        pygame.display.update()
        # print(Points)
        return 'part_1'
