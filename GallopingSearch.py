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


# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,  50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88,
# 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]


# arr = [3, 11, 17, 20, 31, 33, 38, 38, 39, 42, 43, 44, 44, 46, 50]
arr = [i for i in range(1, 100) if i != 49 if i != 79]
print(GallopingSearch(arr, 100))
# self.arr = [1]
# self.arr = [1, 2]
# self.arr = [1]

# arr = [1, 3, 4, 5, 6, 7, 8, 10, 11]
# bi = BinarySearch(arr)
# bi.Step(5)
# print(bi.GetResult())
# bi.Step(5)
# print(bi.GetResult())
# bi.Step(5)
# print(bi.GetResult())
# bi.Step(5)
# print(bi.GetResult())


# arr = [1, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# bi = BinarySearch(arr)
# for i in range (3):
#     bi.Step(2)
# print(bi.GetResult())

#
# arr = [i for i in range(1, 100)]
# bi = BinarySearch(arr)
# bi.Step(101)
# print(bi.GetResult())
# bi.Step(101)
# print(bi.GetResult())
# bi.Step(101)
# print(bi.GetResult())
# bi.Step(101)
# print(bi.GetResult())
# bi.Step(101)
# print(bi.GetResult())
# bi.Step(101)
# print(bi.GetResult())
# bi.Step(101)
# print(bi.GetResult())

# arr = [i for i in range(1, 100)]
# bi = BinarySearch(arr)
# bi.Step(49)
# print(bi.GetResult())
# bi.Step(49)
# print(bi.GetResult())
# bi.Step(49)
# print(bi.GetResult())
# bi.Step(49)
# print(bi.GetResult())
# bi.Step(49)
# print(bi.GetResult())
# bi.Step(49)
# print(bi.GetResult())
# bi.Step(49)
# print(bi.GetResult())
