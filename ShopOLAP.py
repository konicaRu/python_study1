def ShopOLAP(N, items):
    res_dic = {}
    res_arr = []
    name_good = ''
    name_dic = ''
    num_good = ''
    count = 0
    for i in range(len(items)):
        for j in range(len(items[i])):#перебираем строку до пробела
            if items[i][j] != ' ':
                name_good += items[i][j]#коктенируем стоки
            if items[i][j] == ' ':#если пробел
                name_dic = name_good#присваеваем строке отдельную переменную
                count += 1#флаг чтобы не задействовать верхний иф
            if count == 1 and '0' <= items[i][j] <= '9':#перебираем после пробела, только цифры
                num_good += items[i][j]#коктенируем стоку
        if name_dic in res_dic: #если строка(ключ) уже есть в словаре плюсуем значение переведенное в инт
            res_dic[name_dic] += int(num_good)
            name_good = ''
            num_good = ''
            count = 0
        if name_dic not in res_dic:#если строки нету в словаре загоняем в словарь
            res_dic[name_dic] = int(num_good)#добавляем новый ключ и значение
            name_good = ''
            num_good = ''
            count = 0
    for key, value in res_dic.items():#загоняем в массив переменные из словаря
        res_arr.append(key)
        res_arr.append(str(value))#преобразовываем значение в строку
    res_arr_1 = []
    sum = ''
    for i in range(0, len(res_arr), 2):#склеиваем строки попарно
        sum += res_arr[i] + ' ' + str(res_arr[i + 1])
        res_arr_1.append(sum)
        sum = ''
    res_arr_1.sort(reverse=True, key = lambda x: int(x.rsplit(' ',1)[1]))#сортируем по возрастанию знач массива
    return res_arr_1
