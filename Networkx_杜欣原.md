Networkx_杜欣原

要实现的目标：

​	构建一个多重无向图

​	每条边具有权重

​	可以知道每个点的度数，方便找出奇顶点和偶顶点

​	能找到每一个环



---

```Python
G = nx.Graph() # 创建无向图

G = nx.DiGraph() # 创建有向图

G = nx.MultiGraph() # 创建多重无向图

G = nx.MultiDigraph() # 创建多重有向图

G.clear() #清空图
```

---------------------------------------------------------------------------------------------------------------

```Python
#添加节点

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()                 #建立一个空的无向图G（可按需改为创建多重有向图或多重无向图）
G.add_node('a')                  #添加一个节点1
G.add_nodes_from(['b','c','d','e'])    #加点集合
G.add_cycle(['f','g','h','j'])         #加环
H = nx.path_graph(10)          #返回由10个节点挨个连接的无向图，所以有9条边
G.add_nodes_from(H)            #创建一个子图H加入G
G.add_node(H)                  #直接将图作为节点

nx.draw(G, with_labels=True)
plt.show()
```

----------------------------------------------------------------------------------------

```Python
#访问节点

print('图中所有的节点', G.nodes())

print('图中节点的个数', G.number_of_nodes())
```

----

```Python
#删除节点

G.remove_node(1)    #删除指定节点
G.remove_nodes_from(['b','c','d','e'])    #删除集合中的节点

nx.draw(G, with_labels=True)

plt.show()
```

----

```python
#添加边

F = nx.Graph() # 创建无向图
F.add_edge(11,12)   #一次添加一条边

#等价于
e=(13,14)        #e是一个元组
F.add_edge(*e) #这是python中解包裹的过程

F.add_edges_from([(1,2),(1,3)])     #通过添加list来添加多条边

#通过添加任何ebunch来添加边
F.add_edges_from(H.edges()) #不能写作F.add_edges_from(H)

nx.draw(F, with_labels=True)
plt.show()
```

----

```Python
#访问边

print('图中所有的边', F.edges())

print('图中边的个数', F.number_of_edges())
```

----

```Python
#删除边

F.remove_edge(1,2)
F.remove_edges_from([(11,12), (13,14)])

nx.draw(F, with_labels=True)

plt.show()
```

---

```python
#边的属性

G = nx.Graph(day='manday')
G.add_edge(1,2,weight=10)                    #在添加边时分配属性
print(G.edges(data=True))

G.add_edges_from([(1,3), (4,5)], len=22)     #从集合中添加边时分配属性
print(G.edges(data='len'))

G.add_edges_from([(3,4,{'hight':10}),(1,4,{'high':'unknow'})])
print(G.edges(data=True))

G[1][2]['weight'] = 100000                   #通过G[][][]来添加或修改属性
print(G.edges(data=True))
```

---

```python
# 获取节点的度
import networkx as nx

G = nx.Graph()

# add nodes
G.add_node(1, a = 'seds', d = '1.2')
G.add_node(2, a = 'sfdt', d = '1.2')
G.add_node(3, a = 'feds', d = '2.3')
G.add_node(4, a = 'sedf', d = '3.1')

# add edges
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)
G.add_edge(1, 4)

# print
print 'degree of node 1: ', G.degree(1)
print 'degree of node 2: ', G.degree(2)
print 'degree of node 3: ', G.degree(3)
print 'degree of node 4: ', G.degree(4)
```

```Python
# 获取图的边数
import networkx as nx

G = nx.Graph()

# add nodes
G.add_node(1, a = 'seds', d = '1.2')
G.add_node(2, a = 'sfdt', d = '1.2')
G.add_node(3, a = 'feds', d = '2.3')
G.add_node(4, a = 'sedf', d = '3.1')

# add edges
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)
G.add_edge(1, 4)

# print
print 'number of edges:', G.size()
```

