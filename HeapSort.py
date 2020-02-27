class HeapSort:

    def __init__(self):
        self.HeapObject = []  # хранит неотрицательные числа-ключи

    def MakeHeap(self, a):
        self.HeapObject = [None] * len(a)   # создаем итоговый архив с нанами
        if len(a) == 0:
            return
        self.HeapObject[0] = a[0]  # сразу ставим первый элемент
        for i in range(1, len(a)):  # пробегаем  по данным исходного массива начиная со второго тк первый уже вставили
            self.Add(a[i])
        return

    def GetNextMax(self):
        count_N = 0
        for i in self.HeapObject:
            if i == None:
                count_N += 1
        if len(self.HeapObject) == count_N:
            return -1  # если куча пуста состоит из None
        count = 0
        index = 0
        for i in self.HeapObject:
            if i != None:
                count += 1
        root =  self.HeapObject[0]
        self.HeapObject[0] = self.HeapObject[count - 1]
        self.HeapObject[count - 1] = None
        while True:
            if 2 * index + 1 > count - 2 or 2 * index + 2 > count - 2:
                return root
            if self.HeapObject[2 * index + 2] > self.HeapObject[2 * index + 1]:
                swapR = self.HeapObject[index]
                self.HeapObject[index] = self.HeapObject[2 * index + 2]
                self.HeapObject[2 * index + 2] = swapR
                index = 2 * index + 2
            if 2 * index + 1 > count - 2 or 2 * index + 2 > count - 2:
                return root
            if self.HeapObject[2 * index + 2] < self.HeapObject[2 * index + 1]:
                swapL = self.HeapObject[index]
                self.HeapObject[index] = self.HeapObject[2 * index + 1]
                self.HeapObject[2 * index + 1] = swapL
                index = 2 * index + 1

    def Add(self, key):
        count = 0
        if None not in self.HeapObject:
            return False  # если куча вся заполнена
        for i in self.HeapObject:
            if i != None:
                count += 1
        self.HeapObject[count] = key
        while self.HeapObject[count] > self.HeapObject[int((count - 1) / 2)]:  # если элемент больше родителя
            swap = self.HeapObject[int((count - 1) / 2)]  # сохраняем значение родителя в переменной
            self.HeapObject[int((count - 1) / 2)] = self.HeapObject[count]  # меняем значение  родителя на ребенка
            self.HeapObject[count] = swap  # меняем значение ребенка на родителя
            count = int((count - 1) // 2)  # увеличивваем индекс на родительский

        return self.HeapObject

        # УДбРАТЬ ВЫВОД МАССИВА ИЗ return
    # ошибка при максимуме 10 и 5
    # добавление сделать отдельным кодом


a = [110, 90,40, 70,80, 30,10, 20,50, 60,65, 31,29, 11, 9]
# a = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# a = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
#a = [4, 10, 3, 5, 1, 2, 8]
# a = [6, 5, 2, 1, 3, 8, 11, 4, 9, 7]
#a = []
#a = [5,6]
# a = [4, 5] #если 2 элемента придобавлени большего и послед удалением максимального получается неправильная пирамида
# a = [5, 11, 7]
# a = [5, 7, 8]
# a = [5, 7, 8, 4]
#a = [5, 7, 8, 4, 10]
heap = HeapSort()
print(heap.MakeHeap(a))
print(heap.GetNextMax())
print(heap.GetNextMax())
print(heap.GetNextMax())



# print(heap.Add(11))
# должно получиться из [4, 10, 3, 5, 1] -> [10, 5, 3, 4, 1]
# a = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17] -> [17, 15, 13, 9, 6 , 5, 10 , 4, 8, 3, 1]
