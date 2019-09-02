import copy


def BiggerGreater(line):
    arr_line = []  # пустой список для строки
    for i in range(len(line)):  # перебираем строку
        arr_line.append(line[i])  # загоням символы в массив, получаем массив с символами
    arr_chan = copy.copy(arr_line)  # создаем массив в котором будем производить изменения
    arr_chan_1 = []  # создаем пустой массив куда скопируем arr_chan если он окажется ликсиграфически больше исходного
    for i in range(len(arr_line)):
        count = 0  # счетчик итераций
        for j in range(len(arr_line) - 1):
            temp = arr_chan[0 + count]
            arr_chan[0 + count] = arr_chan[1 + count]  # меняем местами первый с последующими элементами
            arr_chan[1 + count] = temp  # меняем местами первый с последующими элементами
            count += 1
            if arr_chan > arr_line:  # сравниваем исходний и получившийся список
                myString = ''.join(arr_chan)  # если получившийся список больше добавляем во временное хранилище
                arr_chan_1.append(myString)
    if arr_chan_1 == []:
        return ''

    return min(arr_chan_1)
