class HeapSort:

    def __init__(self):
        self.HeapObject = []  # хранит неотрицательные числа-ключи

    def  HeapSort(self, a):
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
