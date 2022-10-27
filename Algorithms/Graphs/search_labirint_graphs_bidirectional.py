def create_array_adjacency(quantity_nodes: int):
    """
    Функия создания пустого массива для дальнейшего заполнения графа
    (дополнительная опция, необязательный для вывода)
    """
    array_adjacency = [[0]*quantity_nodes for j in range(quantity_nodes)]
    return array_adjacency

def create_array_visits(quantity_nodes: int):
    """
    Функция создания пустого массива (матрицы смежности)
    для дальнейшего заполнения True в местах построения
    связей между узлами при построении графа
    """
    array_visits = [[0]*quantity_nodes for j in range(quantity_nodes)]
    return array_visits


def search_labirint_graphs(quantity_nodes: int = 10,
                           first_node: list = (0, 1)):
    """
    Функция построения двунаправленного графа с узлами
    """
    import random, copy

    graph, array_adj, array_visits  = [], create_array_adjacency(quantity_nodes), create_array_visits(quantity_nodes)

    y_first_node, x_first_node = first_node[0], first_node[1]
    array_visits[y_first_node][x_first_node] = True
    graph.append(first_node)
    rand_trait = copy.copy(quantity_nodes - 1) # необходимо если надо ставить входное число n-1

    def search_recurent(quantity_nodes):
        if quantity_nodes >= 0:
            n = 0  # переменная для обхода по массиву по оси У
            if n <= quantity_nodes:
                for i in range(3):
                    n += 1
                    k = random.randint(1, rand_trait)  # переменная для определения случайного индекса  в массиве по оси Х
                    if array_visits[quantity_nodes-1][i] == True:
                        continue
                    array_visits[quantity_nodes-1][k] = True
                    node = (quantity_nodes-1, k)
                    graph.append(node)
                    array_adj[quantity_nodes-1][k] = node
            search_recurent(quantity_nodes-1)
    search_recurent(quantity_nodes)

    return graph, array_visits, array_adj


"""
Блок входных данных для вышеуказанной функции
"""
first_option = search_labirint_graphs()

# Создание списка для определения координат узлов на графике
nodes = list()
count_h, count_s, count_r, count_t = 0, 0, 0, 0
for i in range(len(first_option[1])):
    if i < 4:
        nodes.append([100, count_h+100])
        count_h += 80
    elif i >= 4 and i < 8:
        nodes.append([300, count_s + 120])
        count_s += 80
    else:
        nodes.append([250 - count_r, 20 + count_t])
        count_r += 100
        count_t += 440

# Создание графика структуры графа
from graphics import *
win = GraphWin("Graphs", 400, 500)
h, s, r, t = 0, 0, 0, 0
for i in range(len(first_option[1])):
    if i < 4:
        msg = Text(Point(100-50, h+100), f"Node {i}")
        node_point = Circle(Point(100, h+100), 10)
        h += 80
    elif i >= 4 and i < 8:
        msg = Text(Point(300+50, s + 120), f"Node {i}")
        node_point = Circle(Point(300, s + 120), 10)
        s += 80
    else:
        msg = Text(Point(250-r-50, 20+t), f"Node {i}")
        node_point = Circle(Point(250-r, 20+t), 10)
        r += 100
        t += 440
    msg.setSize(12)
    msg.setTextColor("black")
    msg.draw(win)
    node_point.setFill("blue")
    node_point.draw(win)
for i, j in first_option[0]:
    line_node = Line(Point(nodes[i][0], nodes[i][1]), Point(nodes[j][0], nodes[j][1]))
    line_node.setOutline("red")
    line_node.draw(win)
win.getMouse()
win.close()
