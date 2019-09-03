def SherlockValidString(s):
    line_tmp2 = sorted(s)#загоняем строку в массив в алф порядке
    count = 0
    count_rang = 0
    line_tmp = ''
    arr_line = []
    while len(line_tmp2) > 0:#
        if count > 0:
            arr_line.append(line_tmp)#добавляем в массив
            if count > 1:#
                count_rang += 1#
            line_tmp2 = line_tmp2[len(arr_line[count_rang]):]#обрезаем рабочую строку на количество добавл в мас симв
            line_tmp = ''#обнуляем строку
        for j in range(len(line_tmp2)):#ходим по сорт строке загоняем символы в массив группами дублей
            if line_tmp2[j] == line_tmp2[0]:#если дубль
                line_tmp += line_tmp2[j]#коктенируем строку
        count += 1
    arr_line_2 = sorted(arr_line, key=len)#сортируем массив по длинне вход в него строк
    arr_tmp = []
    for i in arr_line_2:#
        arr_tmp.append(len(i))#меняем символы в массиве на их количество, цифровая форма
    count_exc = 0
    count_exc_2 = 0
    for i in range(len(arr_tmp)):
        if i < len(arr_tmp) - 1:#отрабатываем вариант , если все элементы равны
            if arr_tmp[i] == arr_tmp[i + 1]:#
                count_exc += 1
            if count_exc == len(arr_tmp) - 1:
                return True
    for i in range(len(arr_tmp)):
        if i < len(arr_tmp) - 2:#отрабатываем если 1 еденица остальные равны
            if arr_tmp[0] == 1 and arr_tmp[i + 1] == arr_tmp[i + 2]:#
                count_exc_2 += 1
            if count_exc_2 == len(arr_tmp) - 2:
                return True
    if arr_tmp[-2]+1 == arr_tmp[-1]:#отрабатываем если все равны и одна на еденицу больше
        return True
