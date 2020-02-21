def KthOrderStatisticsStep(arr, left, right, k):
    arr_median = []  # массив для хранения медиан
    end = []  # конечный масив для хранения диапазона
    end_left = left  # сохраняем начальную переменную
    while left + 5 <= right:  # идем по массиву с шагом 5
        InsertionSort(arr, left, left + 5)  # каждый под массив из 5 элементов сортируем функцией def InsertionSort(arr, left, right):
        arr_median.append(arr[left + 2])  # медиану маленького подмассива добавляем в массив медиан
        left += 5  # делаем следующий шаг к след подмассиву из 5 элементов
    if left + 5 > right:  # проходим крайний массив который меньше 5 элементов
        InsertionSort(arr, left, right + 1)  # сортируем его
        arr_median.append(arr[(left + right) // 2])  # медиана короткого масива, хвоста? КОГДА В ХВОСТЕ 2 ЭЛЕМЕНТА МЕДИАНОЙ ВЫБИРАЕТСЯ 1 ЭЛЕМЕНТ А ДОЛЖЕН ВТОРОЙ
    InsertionSort(arr_median, 0, len(arr_median))  # сортируем медианы
    s = arr_median[len(arr_median) // 2]  # находим медиану медиан
    for i in range(len(arr)):
        if arr[i] == s:
            if k == i:
                end.append(i)
                return end, arr
            if k > i:
                end.append(i)
                end.append(right)
                return end, arr
            if k < i:
                end.append(end_left)
                end.append(i)
                return end, arr


def InsertionSort(arr, left, right):  # функция для сортировки отрезками подмассивов
    for i in range((left + 1), right):
        new_el = arr[i]
        j = i - 1
        while j >= left and arr[j] > new_el:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = new_el