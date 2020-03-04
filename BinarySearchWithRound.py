class BinarySearch:

    def __init__(self, a):
        self.arr = a
        self.Right = len(self.arr) - 1  # создаем итоговый архив с нанами
        self.Left = 0

    def Step(self, N):
        self.elem_find = 0
        while self.Left <= self.Right:
            pivot = (self.Left + self.Right) // 2
            if  self.arr[pivot] == N: # было впереди self.arr[self.Left] == N or self.arr[self.Right] == N or
                self.elem_find = True
                return
            if self.Left == self.Right:#  if pivot == self.Left or self.Right == pivot:
                self.elem_find = False
                return
            if self.arr[pivot] < N:
                print()
                self.Left = pivot + 1 # было без + 1
            if self.arr[pivot] > N:
                print(0)
                self.Right = pivot - 1 # было без - 1

    def GetResult(self):
        self.Step(N)
        if self.elem_find == True:
            return +1
        if self.elem_find == False:
            return -1



#arr = [1, 3, 4, 5, 6, 7, 8, 10, 11]
#self.arr = [3, 11, 17, 20, 31, 33, 38, 38, 39, 42, 43, 44, 44, 46, 50]
#self.arr = [1]
#self.arr = [1, 2]
#self.arr = [1]

#bi = BinarySearch(arr)
#N = 3
#print(bi.Step(N))
#print(bi.GetResult())
# count = -1
arr = [i for i in range(1, 100)]
bi = BinarySearch(arr)
bi.Step(49)
bi.Step(49)
bi.Step(49)
bi.Step(49)
bi.Step(49)
print(bi.GetResult())