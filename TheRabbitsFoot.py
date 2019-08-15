def TheRabbitsFoot(s, encode):
    if encode == True:
        s = ''.join(s.split())  # убираем пробелы из строки
        root = len(s) ** 0.5  # вычилсяем квадратный корень из кол знаков, возводим в степень 0.5
        num_arr = int(root // 1)  # берем первое число корня
        num_cell = num_arr + 1  # следующую увеличиваем на еденицу
        if num_cell * num_arr < len(s):  # если произведение этих чисел меньше длинны строки
            num_arr += 1  # плюсуем в первому 1
        arr = []  # создаем массив
        descr_line = ''  # создаем строку
        court = 0
        for i in range(num_arr):
            arr.append([])  # добавляем вложенный массив
            for j in range(court, court + num_cell):
                court += 1  # счетчик сколько символов добавили
                if court == len(s) + 1:  # если длинна строки равна добавленным символам останавливаем цикл
                    break
                arr[i].append(s[j])  # добавляем во влож массив символы из s частями, количествами по num_cell
        for i in range(num_cell):
            if i > 0:
                descr_line += ' '
            for j in range(num_arr):
                if j == num_arr - 1 and i >= len(arr[j]):
                    break
                descr_line += arr[j][i]
        return descr_line

    if encode == False:
        ref_line = ''.join(s.split())
        arr_decrip = []
        court2 = 0
        court3 = 0
        court4 = 0
        for k in s:
            if k == ' ':
                court2 += 1
        for i in range(court2 + 1):
            arr_decrip.append([])
            for j in range(court3, len(s)):
                court3 += 1
                if s[j] == ' ':
                    break
                arr_decrip[i].append(s[j])
        scr_line = ''
        for i in range(len(arr_decrip[court4])):
            court4 += 1
            for j in range(len(arr_decrip)):
                if len(ref_line) == len(scr_line):
                    break
                scr_line += arr_decrip[j][i]
        return scr_line
