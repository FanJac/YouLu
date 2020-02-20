import pygame
from pygame.locals import *
from sys import exit
import networkx as nx

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
          [0, 0, 0, 0, 0, 0, 1, 0, 1, 2]]  # 初始化邻接矩阵

# 点，图初始化 dot[0]是起始点
dot = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
edge = [(0, 1), (0, 7), (0, 6), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4), (5, 6), (6, 7), (6, 9), (7, 8), (8, 9)]

# pos是所有点坐标的列表
pos = [(375, 390), (650, 392), (747, 294), (833, 381), (752, 457), (203, 550), (240, 404), (292, 210), (128, 193),
       (86, 412)]

# 判断条件初始化
# pair_dot 是记录每次走的点的队列，pair_dot[0]是起始点，pair_dot[1]是到达点
# still 判断是否执行函数
# edge_judge 存储所有的边，用来判断是否走完所有边，转化为集合是避免顺序的影响例如（1，2）和（2，1）
# pair_dot = [0, None]
# still = False
# counter = 0
# edge_judge = []
# width = 5
# r = 10
# g = nx.MultiGraph()
# g.add_nodes_from(range(10))
# g.add_edges_from(edge)


def change_line_color(screen, still, two_pos, width=5):
    if still:
        pygame.draw.line(screen, GREEN, pos[two_pos[0]], pos[two_pos[1]], width)
        two_pos[0] = two_pos[1]
        two_pos[1] = None

    return two_pos


class part_1_:

    def __init__(self, screen):
        self.screen = screen
        self.current = 0
        self.pair_dot = [0, None]
        self.still = False
        self.counter = 0
        self.edge_judge = []
        for i in edge:
            self.edge_judge.append(set(i))
        self.width = 5
        self.r = 10
        self.g = nx.MultiGraph()
        self.g.add_nodes_from(range(10))
        self.g.add_edges_from(edge)

    # pair_dot = [0, None]
    # still = False
    # counter = 0
    # edge_judge = []
    # width = 5
    # r = 10
    # g = nx.MultiGraph()
    # g.add_nodes_from(range(10))
    # g.add_edges_from(edge)

    def run(self):

        background = pygame.image.load(background_image_file_name).convert()
        self.screen.blit(background, (0, 0))
        for i in edge:
            pygame.draw.line(self.screen, WHITE, pos[i[0]], pos[i[1]], self.width)
        dot[0] = pygame.draw.circle(self.screen, RED, pos[0], self.r)
        for i in range(1, len(dot)):
            dot[i] = pygame.draw.circle(self.screen, GOLD, pos[i], self.r)
        for event in pygame.event.get():

            if event.type == QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in dot:
                    if i.left <= event.pos[0] <= i.left + i.width and i.top <= event.pos[1] <= i.top + i.height:
                        self.pair_dot[1] = dot.index(i)
                        # 判断鼠标点击的点是否与上个点相邻，如果相邻，就执行函数，将两点之间的线染色，并且计数器加1
                        if self.pair_dot[1] in list(nx.neighbors(self.g, self.pair_dot[0])):
                            self.still = True
                            self.counter = self.counter + 1
                            # 从所有边集中移除走过的边，要判断是因为有的边是重复走过，之前就已经删除
                            if set(self.pair_dot) in self.edge_judge:
                                self.edge_judge.remove(set(self.pair_dot))
                            # 如果走回到起始点，判断是否走过所有边，如果已经走完，结束游戏，输出计数器
                            if self.pair_dot[1] == 0:
                                if len(self.edge_judge) == 0:
                                    print(self.counter)
                                    exit()
                        self.pair_dot = change_line_color(self.screen, self.still, self.pair_dot)
                        self.still = False

        # print(TEST)
        # for i in range(2, 11):
        #     for j in range(1, i):
        #         if Points[i-1][j-1] == 1:
        #             pygame.draw.line(self.screen, WHITE, (POINT[i][1], POINT[i][2]), (POINT[j][1], POINT[j][2]), 5)
        # for i in range(1, 11):
        #     if i == 1:
        #         pygame.draw.circle(self.screen, RED, (POINT[i][1], POINT[i][2]), 10, 10)
        #     else:
        #         pygame.draw.circle(self.screen, GOLD, (POINT[i][1], POINT[i][2]), 10, 10)
        pygame.display.update()
        # print(Points)
        return 'part_1'
