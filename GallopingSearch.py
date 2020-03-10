def GallopingSearch(sorted_arr, value):
    if value < sorted_arr[0] or value > sorted_arr[-1]:
        return False
    intermedia_index = 1
    intermedia_value_index = (2 ** intermedia_index) - 2
    if sorted_arr[intermedia_value_index] == value:
        return True
    while True:
        if sorted_arr[intermedia_value_index] == value:
            return True
        if sorted_arr[intermedia_value_index] < value:
            intermedia_index += 1
            intermedia_value_index = (2 ** intermedia_index) - 2
            if intermedia_value_index < len(sorted_arr) - 1:
                if sorted_arr[intermedia_value_index] == value:
                    return True
            if intermedia_value_index > len(sorted_arr) - 1:
                intermedia_value_index = len(sorted_arr) - 1
        if sorted_arr[intermedia_value_index] > value:
            right_boarder = intermedia_value_index
            left_boarder = (2 ** (intermedia_index - 1) - 2) + 1
            bi = BinarySearch(sorted_arr, left_boarder, right_boarder)
            while True:
                bi.Step(value)
                # bi.GetResult()
                if bi.GetResult() != 0:
                    if bi.GetResult() == -1:
                        return False
                    if bi.GetResult() == 1:
                        return True


class BinarySearch:

    def __init__(self, a, Left, Right):
        self.arr = a
        self.Right = Right  # создаем итоговый архив с нанами
        self.Left = Left

    def Step(self, N):
        self.elem_find = 0
        self.pivot = (self.Left + self.Right) // 2
        if self.arr[self.pivot] == N:  # было впереди self.arr[self.Left] == N or self.arr[self.Right] == N or
            self.elem_find = 1
            return
        if self.arr[self.pivot] < N:
            self.Left = self.pivot + 1  # было без + 1
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
            return 1  # , 'Left ==', self.Left, 'Right==', self.Right, 'pivot ==', self.pivot
        if self.elem_find == 2:
            return -1  # , 'Left ==', self.Left, 'Right==', self.Right, 'pivot ==', self.pivot
        if self.elem_find == 0:
            return 0  # , 'Left ==', self.Left, 'Right==', self.Right, 'pivot ==', self.pivot
