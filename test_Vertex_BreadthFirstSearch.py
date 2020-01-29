import unittest
import Vertex_BreadthFirstSearch


class MyTestCase(unittest.TestCase):
    def test_my_peper(self):
        graff = Vertex_BreadthFirstSearch.SimpleGraph(6)
        graff.AddVertex(0)
        graff.AddVertex(1)
        graff.AddVertex(2)
        graff.AddVertex(3)
        graff.AddVertex(4)
        graff.AddVertex(5)
        graff.AddEdge(0, 1)
        graff.AddEdge(0, 2)
        graff.AddEdge(0, 3)
        graff.AddEdge(4, 2)
        graff.AddEdge(1, 2)
        graff.AddEdge(2, 3)
        graff.AddEdge(3, 4)
        self.assertEqual(len(graff.BreadthFirstSearch(0, 4)) == 3, True)
        self.assertEqual(graff.BreadthFirstSearch(0, 4)[0] == graff.vertex[0], True)
        self.assertEqual(graff.BreadthFirstSearch(0, 4)[-1] == graff.vertex[4], True)
        self.assertEqual(graff.BreadthFirstSearch(0, 4)[1] == graff.vertex[2], True)
        self.assertEqual(len(graff.BreadthFirstSearch(0, 5)) == 0, True)

    def test_my_peper2(self):
        graff = Vertex_BreadthFirstSearch.SimpleGraph(6)
        graff.AddVertex(0)
        graff.AddVertex(1)
        graff.AddVertex(2)
        graff.AddVertex(3)
        graff.AddVertex(4)
        graff.AddVertex(5)
        graff.AddEdge(0, 1)
        graff.AddEdge(1, 2)
        graff.AddEdge(3, 4)
        graff.AddEdge(4, 5)
        graff.BreadthFirstSearch(0, 4)
        self.assertEqual(len(graff.BreadthFirstSearch(0, 4)) == 0, True)
        self.assertEqual(len(graff.BreadthFirstSearch(3, 4)) == 2, True)
        self.assertEqual(len(graff.BreadthFirstSearch(3, 5)) == 3, True)
        self.assertEqual(graff.BreadthFirstSearch(3, 4)[0] == graff.vertex[3], True)
        self.assertEqual(graff.BreadthFirstSearch(3, 4)[-1] == graff.vertex[4], True)

    def test_my_peper3(self):
        graff = Vertex_BreadthFirstSearch.SimpleGraph(6)
        graff.AddVertex(0)
        graff.AddVertex(1)
        graff.AddVertex(2)
        graff.AddVertex(3)
        graff.AddVertex(4)
        graff.AddVertex(5)
        graff.AddEdge(0, 1)
        graff.AddEdge(1, 2)
        graff.AddEdge(2, 3)
        graff.AddEdge(3, 4)
        graff.AddEdge(4, 5)
        self.assertEqual(len(graff.BreadthFirstSearch(3, 5)) == 3, True)
        self.assertEqual(graff.BreadthFirstSearch(3, 5)[0] == graff.vertex[3], True)
        self.assertEqual(graff.BreadthFirstSearch(3, 5)[-1] == graff.vertex[5], True)



if __name__ == '__main__':
    unittest.main()
