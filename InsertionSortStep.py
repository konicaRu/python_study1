def InsertionSortStep(array, step=0, ind=0):
    if step == 1:
        for i in range(ind, len(array)):
            LocalMin = array[i]
            j = i - 1
            while j >= ind and array[j] > LocalMin:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = LocalMin
        return array
    else:
        for i in range(ind, len(array)):
            LocalMin = array[i]
            j = i + step
            while j + step <= len(array) - 1:
                j += step
            if j > len(array) - 1:
                return array
            if i == ind and array[i] > array[j]:
                array[i] = array[j]
                array[j] = LocalMin
            if array[i] > array[j] and array[i - 1] < array[j]:
                array[i] = array[j]
                array[j] = LocalMin


# print(InsertionSortStep([4, 3, 1, 2], 3, 0))
#print(InsertionSortStep([7, 6, 5, 4, 3, 2, 1], 3, 0))
print(InsertionSortStep([1, 6, 5, 4, 3, 2, 7], 1, 1))
