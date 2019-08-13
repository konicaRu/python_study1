def WordSearch(widht_str, s, subs):
    court = 0  # счетчик длинны предидущей строки
    court1 = 0  # счетчик операци за один проход на более widht_str
    court_all = 0  # общий счетчик операцииъ
    court_speace = 0  # добавляем пропушенный пробел в строке 13
    add_str = ''
    sum_arr = []
    line_length = 0
    j = 0
    len_frases = len(s)
    for i in range(len_frases):
        while j < len(s) - 1:
            if s[court] == ' ':  # проскакиваем пробел начинаем подсчет со след позиции(с символа)
                court += 1
                court_speace = 1  # добавляем пропущенный пробел в счетчик line_lenght
                # бегаем по строке необходимое количество отрезков
            for j in range(0 + court, widht_str + court):  # перебебираем символы истрокезаданными диапазонами widht_str
                court_all += 1
                court1 += 1
                add_str += s[j]  # коктенация строки
                if j == len(s) - 1:  # добавляем последнее слово
                    sum_arr.append(add_str)
                    break
                if widht_str == court1:
                    if add_str.find(' ') == -1 and s[((line_length+court_speace) + court1)] != ' ':
                        sum_arr.append(add_str)
                    if add_str.find(' ') != -1 and s[((line_length+court_speace) + court1)] != ' ':
                        for k in range(len(add_str) - 1, -1, -1):  # перебираем строку с конца до пробела
                            if add_str[k] == ' ':  # проверяем не закинчивается ли строка
                                add_str = add_str[0:k]  # пробелом или следующий символ не пробел ли?
                                sum_arr.append(add_str)
                                break
                    if s[((line_length+court_speace) + court1)] == ' ':
                        sum_arr.append(add_str)
                    line_length += len(add_str) + court_speace  # длинна текущей строки
                    court += len(add_str)  # и добавляем пробелы которые пропустили
                    add_str = ''
                    court1 = 0
                    court_speace = 0
    end_arr = []
    for h in sum_arr:
        if subs in h.split():
            end_arr.append(1)
        else:
            end_arr.append(0)

    return end_arr