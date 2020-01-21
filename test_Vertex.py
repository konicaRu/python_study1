import unittest
import Vertex


class MyTestCase(unittest.TestCase):
    def test_AddVertex(self):#вершина имеется, связи с ней отсутствуют
        graff = Vertex.SimpleGraph(4)
        graff.AddVertex(1)
        self.assertEqual(graff.vertex.count(None) == len(graff.vertex) - 1, True)#считает количкество Нан в масисиве
        self.assertEqual(graff.m_adjacency.count(1) == 0, True) #проверяет количество связей (едениц) в матрице
        graff.AddVertex(3)
        self.assertEqual(graff.vertex.count(None) == len(graff.vertex) - 2, True)
        self.assertEqual(graff.m_adjacency.count(1) == 0, True)

    def test_AddEdge(self):
        graff = Vertex.SimpleGraph(4)# до добавления связи между вершинами не было, после добавления появилась
        graff.AddVertex(1)
        graff.AddVertex(2)
        graff.AddVertex(3)
        graff.AddVertex(4)
        self.assertEqual(graff.m_adjacency[1][2] == 0, True)
        self.assertEqual(graff.m_adjacency[2][1] == 0, True)
        graff.AddEdge(1, 2)
        self.assertEqual(graff.m_adjacency[1].count(1) == 1, True)#считает количкество едениц в масисиве
        self.assertEqual(graff.m_adjacency[2].count(1) == 1, True)
        self.assertEqual(graff.m_adjacency[1][2] == 1, True)
        self.assertEqual(graff.m_adjacency[2][1] == 1, True)

    def test_RemoveEdge(self):
        graff = Vertex.SimpleGraph(4) # до удаления связь между вершинами была, после удаления отсутствует
        graff.AddVertex(1)
        graff.AddVertex(2)
        graff.AddVertex(3)
        graff.AddVertex(4)
        graff.AddEdge(1, 2)
        self.assertEqual(graff.m_adjacency[1][2] == 1, True)
        self.assertEqual(graff.m_adjacency[2][1] == 1, True)
        graff.RemoveEdge(1, 2)
        self.assertEqual(graff.m_adjacency[1][2] == 0, True)
        self.assertEqual(graff.m_adjacency[2][1] == 0, True)

    def test_RemoveVertex(self):
        graff = Vertex.SimpleGraph(4)# до удаления некоторые вершины имеют связи с удаляемой вершиной, после удаления этих связей нету
        graff.AddVertex(1)
        graff.AddVertex(2)
        graff.AddVertex(3)
        graff.AddVertex(4)
        graff.AddEdge(1, 2)
        #до удаления
        self.assertEqual(graff.vertex.count(None) == 0, True)  # считает количкество Нан в масисиве
        self.assertEqual(graff.m_adjacency[1].count(0) == 3, True)  # считает количкество едениц в масисиве до добавления связей
        self.assertEqual(graff.m_adjacency[2][1] == 1, True)
        self.assertEqual(graff.m_adjacency[1][2] == 1, True)
        graff.RemoveVertex(1)
        #после удаления
        self.assertEqual(graff.vertex.count(None) ==  1, True)  # считает количкество Нан в масисиве
        self.assertEqual(graff.m_adjacency[1].count(0) == 4, True)  # считает количкество едениц в масисиве до добавления связей
        self.assertEqual(graff.m_adjacency[2][1] == 0, True)
        self.assertEqual(graff.m_adjacency[1][2] == 0, True)

if __name__ == '__main__':
    unittest.main()
