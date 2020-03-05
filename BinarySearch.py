class BinarySearch:

    def __init__(self, a):
        self.arr = a
        self.Right = len(self.arr) - 1  # создаем итоговый архив с нанами
        self.Left = 0


    def Step(self, N):
        self.elem_find = 0
        pivot = (self.Left + self.Right) // 2
        if self.arr[pivot] == N:  # было впереди self.arr[self.Left] == N or self.arr[self.Right] == N or
            self.elem_find = 1
            return
        if self.Left == self.Right:  # if pivot == self.Left or self.Right == pivot:
            self.elem_find = 2
            return
        if self.arr[pivot] < N:
            self.Left = pivot + 1  # было без + 1
        if self.arr[pivot] > N:
            self.Right = pivot - 1  # было без - 1
        if self.Left > self.Right:
            self.elem_find = 2
            return


    def GetResult(self):
        if self.elem_find == 1:
            return  '+1'
        if self.elem_find == 2:
            return -1
        if self.elem_find == 0:
            return 0
