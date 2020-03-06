class BinarySearch:

    def __init__(self, a):
        self.arr = a
        self.Right = len(self.arr) - 1  # создаем итоговый архив с нанами
        self.Left = 0


    def Step(self, N):
        self.elem_find = 0
        self.pivot = (self.Left + self.Right) // 2
        if self.arr[self.pivot] == N:  # было впереди self.arr[self.Left] == N or self.arr[self.Right] == N or
            self.elem_find = 1
            return
        if self.arr[self.pivot] < N:
            self.Left = self.pivot + 1 # было без + 1
        if self.arr[self.pivot] > N:
            self.Right = self.pivot - 1  # было без - 1
        if self.arr[self.Left] == self.arr[self.Right] == N:  # if pivot == self.Left or self.Right == pivot:
            self.elem_find = 1
            return
        if self.arr[self.Left] == self.arr[self.Right] != N or (self.Left + 1 == self.Right and self.arr[self.Left] != N and self.arr[self.Right] != N):  # if pivot == self.Left or self.Right == pivot:
            self.elem_find = 2
            return
        if self.Left > self.Right:
            self.elem_find = 2
            return


    def GetResult(self):
        if self.elem_find == 1:
            return  1 #, 'Left ==', self.Left, 'Right==', self.Right, 'pivot ==', self.pivot
        if self.elem_find == 2:
            return -1 #, 'Left ==', self.Left, 'Right==', self.Right, 'pivot ==', self.pivot
        if self.elem_find == 0:
            return 0 #, 'Left ==', self.Left, 'Right==', self.Right, 'pivot ==', self.pivot
