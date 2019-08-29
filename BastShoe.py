arr_indicat = []  # массив для хранения индикаторов выпонения операц 1 добавить или 2 удалить
gen_line = ''  # основная строка
add_line = []  # строка для хранения добавленных элементов
del_line = []  # строка для хранения удаленных элементов
redo_line = []  # накапливаем элементы для REDO(выполнить заново последнюю отменённую с помощью Undo операцию)
count_reset = 0


def BastShoe(N):
    num = int(N[0])  # отделяем первую цифру
    if num <= 0 or num > 5:  #
        return 'Wrong enter'
    global add_line
    global del_line
    global gen_line
    global count_reset
    if num == 1:  # условие работы алгоритма Добавить в конец текущей строки (исходно пустая) добавляется строка S;
        if count_reset > 0:  # по маркеру сброса предыдущая цепочка операций для Undo обнуляется
            add_line.clear()
            redo_line.clear()
            del_line = []
        gen_line += N[2:]  # убираем из введенной строки цифру и пробел, 2 первых знака
        add_line.append(N[2:])  # добавляем в строку хранения добавленных элементов add_line
        arr_indicat.append(1)  # добавляем индикатор произведенного действия 1 в arr_indicat
        return gen_line
    if num == 2:  # 2. Удалить(N) -- удалить N символов из конца текущей строки;
        if count_reset > 0:  # по маркеру сброса предыдущая цепочка операций для Undo обнуляется
            add_line.clear()  # очищаем массивы буфера
            redo_line.clear()
            del_line.clear()
        remov = int(N[2:]) * -1  # сколько знаков будем удалять
        del_line.append(gen_line[remov:])  # добавляем удаленные знаки в массив для возможной отмены операции
        gen_line = gen_line[:remov]  # удаляем из основной строки
        arr_indicat.append(2)  # ставим маркер какая 4 сработает
        return gen_line
    if num == 3:
        if int(N[2:]) <= len(gen_line) - 1:  # выдать i-й символ текущей строки (индексация начинается с нуля)
            return gen_line[int(N[2:])]  # в форме стр. Если индекс за пределами строки, возвращайте пустую строку;
    if num == 4 and arr_indicat[-1] == 1:  # UNDO отмена последней операции 1 добавление
        if not add_line:  # если список добавленных элементов пуст печатаем строку
            return gen_line
        gen_line = gen_line[:len(add_line[-1]) * -1]  # убираем добавл строку считывая последний эл add_line[-1]
        del_line.append(add_line[-1])  #
        redo_line.append(del_line[-1])  # добавляем элемент для REDO
        del arr_indicat[-1]  # сбрасываем индикатор на одно действие, удаляем последний элемент массива
        del add_line[-1]  # удаляем из накопительного массива последний элемент
        count_reset = 1  # ставим маркер сброса предыдущая цепочка операций для Undo обнуляется
        return gen_line
    if num == 4 and arr_indicat[-1] == 2:  # UNDO отмена последней операции  2; удаление
        gen_line += del_line[-1]  # добавляем удаленную строку из буфера
        redo_line.append(del_line[-1])  # и добавляем ее в редо если последует отмена
        del del_line[-1]  # удаляем добавленную часть из буфера массива
        del arr_indicat[-1]  # убираем индикатор
        count_reset = 2  # ставим маркер сброса предыдущая цепочка операций для Undo обнуляется
        return gen_line
    if num == 5:  # REDO выполнить заново последнюю отменённую с помощью Undo операцию
        if not redo_line:  # если список добавленных элементов пуст печатаем строку
            return gen_line
        if count_reset == 2:  # маркер если пред отменой было отмена удаления
            gen_line = gen_line[:len(redo_line[-1]) * -1]  # удаляем приставленный конец
            del redo_line[-1]  # убираепм из буфера!! может надо добавить смену индикатора???
            return gen_line
        gen_line += redo_line[-1]  # если пред отменой была отмена добавлния
        add_line.append(redo_line[-1])  # добавляем отмененное в строку
        arr_indicat.append(1)  # меняем индиккатор
        del redo_line[-1]  # убираепм из буфера!!
    return gen_line
