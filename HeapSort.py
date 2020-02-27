class HeapSort:

    def __init__(self, a):
        self.arr = a
        self.HeapObject = [None] * len(self.arr)  # создаем итоговый архив с нанами
        self.HeapObject[0] = self.arr[0]
        for i in range(1, len(self.arr)):  # пробегаем  по данным исходного массива начиная со второго тк первый уже вставили
            self.Add(a[i])

    def GetNextMax(self):
        if len(self.HeapObject) == self.HeapObject.count(None):
            return -1
        count = len(self.HeapObject) - self.HeapObject.count(None)
        index = 0
        root = self.HeapObject[0]
        self.HeapObject[0] = self.HeapObject[count - 1]
        self.HeapObject[count - 1] = None
        while True:  # if self.HeapObject[2]== None and self.HeapObject[0] < self.HeapObject[1]  меняем местами
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
        count = len(self.HeapObject) - self.HeapObject.count(None)
        if None not in self.HeapObject:
            return False  # если куча вся заполнена
        self.HeapObject[count] = key
        while self.HeapObject[count] > self.HeapObject[int((count - 1) / 2)]:  # если элемент больше родителя
            swap = self.HeapObject[int((count - 1) / 2)]  # сохраняем значение родителя в переменной
            self.HeapObject[int((count - 1) / 2)] = self.HeapObject[count]  # меняем значение  родителя на ребенка
            self.HeapObject[count] = swap  # меняем значение ребенка на родителя
            count = int((count - 1) // 2)  # увеличивваем индекс на родительский
