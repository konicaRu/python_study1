class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов
        self.level = 1


class SimpleTree:

    def __init__(self, root):
        self.Root = root;  # корень, может быть None

    def AddChild(self, ParentNode, NewChild):
        ParentNode.Children.append(NewChild)  # ParentNode.Children = NewChild
        NewChild.Parent = ParentNode
        NewChild.level = ParentNode.level + 1

    def EvenTrees(self):
        res = []# надо предусмотреть если корень нана или только один корень
        stack = []
        node = self.Root
        if node == None:
            return res
        for i in range(len(node.Children)):
            vizit = []
            vizit.append(node)
            stack.insert(0, node.Children[i])
            while len(stack) != 0:
                for j in stack[0].Children:
                    stack.append(j)
                vizit.insert(0, stack[0])
                stack.pop(0)
                if len(stack) == 0:
                    if len(vizit) % 2 == 1:
                        res.append(node)
                        res.append(node.Children[i])

        return res
