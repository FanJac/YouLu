import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import itertools

# 生成例图
G = nx.MultiGraph()
V = [1, 2, 3, 4, 5, 6, 7]
G.add_nodes_from(V)
E = [(1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (4, 5), (4, 7), (5, 7)]
G.add_edges_from(E)
# key_points:在一个有奇度数结点的赋权连通图中，增加一些平行边，使得新图不含奇度数结点，并且增加的边的总权值最小。
# 找出奇点
odd = []
for i in G.nodes():
    if G.degree(i) % 2 == 1:
        odd.append(i)
print('odd', odd)
# 奇点之间的最短路径
path = []
path1 = {}
path2 = {}
distance = np.zeros((len(odd), len(odd)))
for i in odd:
    for j in odd[odd.index(i) + 1:]:
        k = nx.shortest_path(G, i, j)
        path.append([(i, j), len(k)-1, k]) # [(i,j), num] 中(i,j)代表奇点i和奇点j, num代表两个奇点之间的最短距离
for i in path:
    path1[i[0]] = i[1]
for i in path:
    path2[i[0]] = i[2]
# path1 储存每对奇点之间最短距离
# path2 储存每对奇点之间最短路径
print('path1', path1)
print('path2', path2)
# 遍历求最短路程(考虑是否可以优化）
# 遍历所有奇点的匹配
combination = list(itertools.permutations(odd, len(odd)))
match1 = []
match = []
for i in combination:
    save = []
    j = 0
    while True:
        pair = [i[j], i[j+1]]
        pair.sort()
        pair = tuple(pair)
        save.append(pair)
        j = j + 2
        if j == len(i):
            break
    save.sort()
    match1.append(save)
for i in match1:
    if i not in match:
        match.append(i)
print('match', match)
# 求出每个奇点匹配对应的路径长度，并求出最小值
values = {}
for i in match:
    value = 0
    for j in i:
        value = value + path1[j]
    values[tuple(i)] = value
print('values', values)
shortest = min(values)
shortest_value = values[shortest]
print(shortest, shortest_value)
# 得到最短距离
solution = len(G.edges) + shortest_value
print(solution)
# 得到最短路径
for i in shortest:
    way = []
    k = 0
    j = path2[i]
    while True:
        way.append((j[k], j[k+1]))
        k = k + 1
        if k == len(j) - 1:
            break
    G.add_edges_from(way)
print(list(G.edges))

