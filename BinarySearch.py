class BinarySearch:

    def __init__(self, arr):
        self.Right = len(arr) - 1  # создаем итоговый архив с нанами
        self.Left = 0

    def Step(self, N):
        self.elem_find = 0
        while True:
            pivot = (self.Left + self.Right) // 2
            if arr[self.Left] == N or arr[self.Right] == N or arr[pivot] == N:
                self.elem_find = True
                return
            if self.Left == self.Right:
                self.elem_find = False
                return
            if pivot == self.Left or self.Right == pivot:
                self.elem_find = False
                return
            if arr[pivot] < N:
                print(0)
                self.Left = pivot
            if arr[pivot] > N:
                print(0)
                self.Right = pivot

    def GetResult(self):
        self.Step(N)

        if self.elem_find == True:
            return +1
        if self.elem_find == False:
            return -1

