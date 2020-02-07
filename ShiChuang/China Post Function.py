import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import itertools


# 图的顶点必须由不同的整数表示
def solution_of_cp(node, edge):
    graph = nx.MultiGraph()
    graph.add_edges_from(edge)
    graph.add_nodes_from(node)
    odd = []
    for i in graph.nodes():
        if graph.degree(i) % 2 == 1:
            odd.append(i)                   # 找出奇点
    odd.sort()
    path = []
    path1 = {}
    path2 = {}
    for i in odd:
        for j in odd[odd.index(i) + 1:]:
            k = nx.shortest_path(graph, i, j)
            path.append([(i, j), len(k) - 1, k])  # [(i,j), num] 中(i,j)代表奇点i和奇点j, num代表两个奇点之间的最短距离
    for i in path:
        path1[i[0]] = i[1]
    for i in path:
        path2[i[0]] = i[2]
    combination = list(itertools.permutations(odd, len(odd)))
    match1 = []
    match = []
    for i in combination:
        save = []
        j = 0
        while True:
            pair = [i[j], i[j + 1]]
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
    values = {}
    for i in match:
        value = 0
        for j in i:
            value = value + path1[j]
        values[tuple(i)] = value
    shortest = min(values)
    shortest_value = values[shortest]
    solution = len(graph.edges) + shortest_value
    for i in shortest:
        way = []
        k = 0
        j = path2[i]
        while True:
            way.append((j[k], j[k + 1]))
            k = k + 1
            if k == len(j) - 1:
                break
        graph.add_edges_from(way)
    return [graph, solution]
