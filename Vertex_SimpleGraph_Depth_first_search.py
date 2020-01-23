class Vertex:

    def __init__(self, val):
        self.Value = val
        self.hit = False


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

    def DepthFirstSearch(self, VFrom, VTo):# поиск в глубину
        res = []
        node = self.m_adjacency[VFrom]# показываем указателем на начало поиска
        res.append(self.vertex[VFrom])# добавляем его в список первым
        self.vertex[VFrom].hit = True # присваяваем графу флажок просмотрен
        count = -1 # счетчик итераций
        while True:
            for i in node: # пробегаем по массиву матрицы на который указывает указатель находя первое ребро в списке
                count += 1
                if count > len(node) - 1:# почему то for не ограничивался длинной массива матрицы а бежал дальще это костыль чтобы его остановить в пределах массива, если новых ребер нет
                    res.pop()# удаляем граф из стека
                    if res == []:# если список пустой все графы удалены искомый узел не найден
                        return []
                    node = self.m_adjacency[len(res) - 1]# переводим указатель на следуюший граф от удаленного
                    count = -1
                    break # возвращаемся на фор и еще раз пробегаем узел на который указывает указатель нода
                if i == 1 and count == VTo:# усли индекс ребра равен искомому узлу добавляем его в список и выходим из фукцции с путем к искомой ноде
                    res.append(self.vertex[VTo])
                    return res
                if i == 1 and count != VTo and self.vertex[count].hit == False: #нашли граф не просмотренный не конечный 
                    res.append(self.vertex[count])# добавляем в список
                    self.vertex[count].hit = True # # присваяваем графу флажок просмотрен
                    node = self.m_adjacency[count] # переводим указатель на следующий список ребер графа
                    count = -1 # обнуляем счетчик
                    break # запуская цикл for  заново
