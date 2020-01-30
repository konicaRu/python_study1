class Vertex:

    def __init__(self, val):
        self.Value = val
        self.hit = False
        self.level = 0


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v):
        for i in range(len(self.vertex)):
            if self.vertex[i] == None:
                self.vertex[i] = Vertex(v)
                return
            if self.vertex[i] != None:
                continue
        return

    def RemoveVertex(self, v):
        self.vertex[v] = None  # ваш код удаления вершины со всеми её рёбрами
        for i in range(len(self.m_adjacency[v])):
            if self.m_adjacency[v][i] != 0:
                self.m_adjacency[v][i] = 0
        for j in range(len(self.m_adjacency)):
            if self.m_adjacency[j][v] == 1:
                self.m_adjacency[j][v] = 0
        return

    def IsEdge(self, v1, v2):
        if self.m_adjacency[v1][v2] == 1 and self.m_adjacency[v2][v1] == 1:
            return True
        else:  # True если есть ребро между вершинами v1 и v2
            return False

    def AddEdge(self, v1, v2):  # предусмотреть выход за диапазон списка
        self.m_adjacency[v1][v2] = 1  # добавление ребра между вершинами v1 и v2
        self.m_adjacency[v2][v1] = 1
        return

    def RemoveEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 0  # удаление ребра между вершинами v1 и v2
        self.m_adjacency[v2][v1] = 0
        return

    def DepthFirstSearch(self, VFrom, VTo):
        res = []
        node = self.m_adjacency[VFrom]
        res.append(self.vertex[VFrom])
        self.vertex[VFrom].hit = True
        count = -1
        while True:
            for i in node:
                count += 1
                if count > len(node) - 1:
                    res.pop()
                    if res == []:
                        return []
                    node = self.m_adjacency[len(res) - 1]
                    count = -1
                    break
                if i == 1 and count == VTo:
                    res.append(self.vertex[VTo])
                    return res
                if i == 1 and count != VTo and self.vertex[count].hit == False:
                    res.append(self.vertex[count])
                    self.vertex[count].hit = True
                    node = self.m_adjacency[count]
                    count = -1
                    break

    def BreadthFirstSearch(self, VFrom, VTo):
        if self.m_adjacency[VFrom].count(0) == len(self.m_adjacency) or self.m_adjacency[VTo].count(0) == len(self.m_adjacency):  # если у начального и конечного элемента
            return []  # нет связей с остальными
        if VFrom == VTo:
            if self.m_adjacency[VFrom].count(0) == len(self.m_adjacency):
                return []
            else:
                return [self.vertex[VFrom], self.vertex[VTo]]
        res = []
        res.append(self.vertex[VFrom])  # добавляем в итоговый-промежуточный массив графф с которого начинаем поиск
        count_graf = -1
        for i in res:  # бежим по этому списку
            if i.hit != True:  # пробегаем по нему если стоит отметка что еще не смотрели hit != True
                i.hit = True  # ставим флаг что просмотрено
                for j in self.m_adjacency[self.vertex.index(i)]:  # пробегаем по массиву где ребра этого графа
                    count_graf += 1
                    if j == 1 and self.vertex[count_graf].hit != True and self.vertex[count_graf] not in res:  # если есть ребро и соответственно смежный граф
                        res.append(self.vertex[count_graf])  # добавляем его в итоговый промежуточный список
                        self.vertex[count_graf].level = i.level + 1  # ставим отметку какой уровень
                count_graf = -1  # при выходе из цикла сбрасываем счетчик
        res_way = []
        res_way.insert(0, self.vertex[VTo])
        index_way = VTo
        count_way = -1
        while True:
            for i in self.m_adjacency[index_way]:
                count_way += 1
                if i == 1:
                    if self.vertex[count_way].level == 0:
                        res_way.insert(0, self.vertex[count_way])
                        if self.vertex[VFrom] not in res_way or self.vertex[VTo] not in res_way:  # если начальный и конечный элемент не входят в итоговый список значит пути нет
                            for k in self.vertex:
                                k.level = 0
                                k.hit = False
                            return []
                        else:
                            for k in self.vertex:
                                k.level = 0
                                k.hit = False
                            return res_way
                    if self.vertex[count_way].level == self.vertex[index_way].level - 1 and self.vertex[count_way] not in res_way:
                        res_way.insert(0, self.vertex[count_way])
                        index_way = count_way
                        count_way = -1
                        break
