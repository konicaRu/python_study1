def InsertionSortStep(array, step=1, ind=0):
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
        # for i in range(ind, len(array)):
        i = ind
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
        return array


def KnuthSequence(array):
    count = 1
    res = [1]
    while count <= len(array):
        count = 3 * count + 1
        if count > len(array):
            return res
        res.insert(0, count)



# print(InsertionSortStep([4, 3, 1, 2], 3, 0))
# print(InsertionSortStep([7, 6, 5, 4, 3, 2, 1], 3, 0))
# print(InsertionSortStep([1, 6, 5, 4, 3, 2, 7], 3, 2))
print(KnuthSequence([i for i in range(1,50)]))
