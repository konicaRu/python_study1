class Heap:

    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи

    def MakeHeap(self, a, depth):
        self.HeapArray =[None] * (2 ** (depth + 1) - 1)# создаем итоговый архив с нанами
        if len(a) == 0:
            return self.HeapArray
        a = a[::-1] # переворачиваем массив чтобы работать с последнего элемента
        self.HeapArray[0] = a[0] #сразу ставим первый элемент
        for i in range(1, len(a)): # пробегаем  по данным исходного массива насиная со второго тк первый уже вставили
            self.HeapArray[i] = a[i] # вставляем элемент на первое свободное поле
            while self.HeapArray[i] > self.HeapArray[int((i-1) / 2)]: #если элемент больше родителя
                swap = self.HeapArray[int((i-1) / 2)] # сохраняем значение родителя в переменной
                self.HeapArray[int((i-1) / 2)] = self.HeapArray[i] #меняем значение  родителя на ребенка
                self.HeapArray[i] = swap #меняем значение ребенка на родителя
                i = int((i-1) // 2) # увеличивваем индекс на родительский

        # создаём массив кучи HeapArray из заданного
        # размер массива выбираем на основе глубины depth
        return self.HeapArray

    def GetMax(self):
        count = 0
        for i in self.HeapArray:
            if i == None:
                count +=1
        if len (self.HeapArray) == count:
            return -1  # если куча пуста состоит из None
        if len(self.HeapArray) - 1 == count: # если куча  состоит из одного элемента
            return -1
        count = 0
        index = 0
        for i in self.HeapArray:
            if i == None:
                count += 1
        del self.HeapArray[-count:-1]
        del self.HeapArray[-1]
        self.HeapArray[0] = self.HeapArray[ - 1]
        self.HeapArray.pop(-1)
        while  True:
            if 2 * index + 1 > len(self.HeapArray) - 1 or 2 * index + 2 > len(self.HeapArray) - 1:
                swapR = self.HeapArray[index]
                self.HeapArray[index] = self.HeapArray[-1]
                self.HeapArray[-1] = swapR
                return self.HeapArray[0], self.HeapArray
            if self.HeapArray[2 * index + 2] > self.HeapArray[2 * index + 1] :
                swapR = self.HeapArray[index]
                self.HeapArray[index] = self.HeapArray[2 * index + 2]
                self.HeapArray[2 * index + 2] = swapR
                index = 2 * index + 2
            if 2 * index + 1 > len(self.HeapArray)-1 or 2 * index + 2 > len(self.HeapArray)-1:
                    swapR = self.HeapArray[index]
                    self.HeapArray[index] = self.HeapArray[-1]
                    self.HeapArray[-1] = swapR
                    return self.HeapArray[0], self.HeapArray
            if self.HeapArray[2 * index + 2] < self.HeapArray[2 * index + 1] :
                swapL = self.HeapArray[index]
                self.HeapArray[index] = self.HeapArray[2 * index + 1]
                self.HeapArray[2 * index + 1] = swapL
                index = 2 * index + 1

        # вернуть значение корня и перестроить кучу

    def Add(self, key):
        arr = []
        if None  not in self.HeapArray:
            return False  # если куча вся заполнена
        for i in self.HeapArray:
            if i != None:
                arr.append(i)
        arr.append(key)
        return self.MakeHeap(arr, int(len(self.HeapArray)**0.5))
