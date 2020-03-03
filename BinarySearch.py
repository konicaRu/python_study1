class BinarySearch:

    def __init__(self, arr):
        self.Right = len(arr) - 1  # создаем итоговый архив с нанами
        self.Left = 0

    def Step(self, N):
        self.elem_find = 0
        while True:
            pivot = (self.Left + self.Right) // 2
            if self.Left == self.Right:
                self.elem_find = False
                return
            if arr[self.Left] == N or arr[self.Right] == N or arr[pivot] == N:
                self.elem_find = True
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


# arr = [1,  3, 4, 5, 6, 7, 8, 9, 10]
# N = 3
# bi = BinarySearch(arr)
# bi.Step(N)
# print(bi.GetResult())
count = -1
arr = [i for i in range(100000)]
arr.pop(200)
N = 5000
bi = BinarySearch(arr)
print(bi.Step(N))
print(bi.GetResult())
