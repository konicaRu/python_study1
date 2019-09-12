import copy
def Football(F, N):
    count_lev1 = -1 #счетчик второго массива
    count_lev2 = 0
    check_F = sorted(F)#создаем сортированную копию списка как эталон для сравнения
    arr_tmp = copy.copy(F)#создаем копию списка для перестановки
    for i in range(len(F) - 1): # двигаем первий диапазон
        count_lev1 += 1
        for j in range(count_lev1, len(F)-1): # двигаем второй диапазон по списку
            count_lev2 += 1
            tmp_var = arr_tmp[j + 1]#сохраняем значение во временную переменную
            arr_tmp[j + 1] = arr_tmp[i]
            arr_tmp[i] = tmp_var
            if arr_tmp == check_F: # сравниваем получился ли список эквивалентен эталонному
                return True # если да способ сработал
            else:
                arr_tmp = copy.copy(F)# если нет возвращаем список в исходный вариант
    count_lev1 = 0  # счетчик второго массива
    check_F = sorted(F)  # создаем сортированную копию списка как эталон для сравнения
    arr_tmp = copy.copy(F)  # создаем копию списка для перестановки
    arr_rever = copy.copy(F)  # создаем копию списка для проверки полной обратности
    arr_rever.reverse()  # разворачиваем список
    if len(F) > 3:  # если длинна меньше то отрабатыает первый алгоритм
        if check_F == arr_rever:  # сравнивае6м список эталонным
            return True
    for i in range(len(F) - 3):  # двигаем первий диапазон
        count_lev1 += 1
        for j in range(count_lev1 + 3, len(F) + 1):  # двигаем второй диапазон по списку
            arr_tmp_lev2 = arr_tmp[i:j]  # ВНИМАНИЕ! Выделяем слайс в отдельный массив
            arr_tmp_lev2.reverse()  # разворачиваем слайс
            arr_tmp[i:j] = arr_tmp_lev2  # вставляем слайс на тоже место в массив
            if arr_tmp == check_F:  # сравниваем получился ли список эквивалентен эталонному
                return True  # если да способ сработал
            else:
                arr_tmp = copy.copy(F)  # если нет возвращаем список в исходный вариант

