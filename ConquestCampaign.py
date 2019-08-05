def ConquestCampaign(N, M, L, battalion):
    court_land = 0
    vert_land = 0
    goriz_land = 0
    court_day = 0
    court_day1 = 0
    court_day2 = 1
    a = []
    for i in range(N):  # создаем марицу из нулей N-строк (количество массивов), М-столбцов(элементов массива
        b = []
        for j in range(M):
            b.append(0)
        a.append(b)
    for j in range(len(battalion)):  # раставляем еденицы по координатам
        court_land += 1
        if court_land == 1:
            vert_land = battalion[j]
        if court_land == 2:
            goriz_land = battalion[j]
        if court_land == 2 and battalion[j] == battalion[j - 1]:  # если если координаты совпадают то они равны
            vert_land = battalion[j]
            goriz_land = battalion[j]
        if court_land == 2:  # координаты считаны
            a[vert_land - 1][goriz_land - 1] = 1  # выставляем еденицу по координате
            court_land = 0  # обнуляем счетчик и координаты
            vert_land = 0
            goriz_land = 0
    for h in range(len(a)):  # проверяем бегаем по списку ищем нули, если свободные места есть заполняем
        for k in a[h]:
            if k == 0:
                court_day += 1
                court_day1 += 1
                court_day2 += 1
                h == 0
                for i in range(0, len(a)):
                    for j in range(0, len(a[i])):  # если нули есть бегаем по списку заполняем свободные клетки
                        if a[i][j] == court_day1:  # по очереди первая координата 1 вторая 2 и так далее
                            if 0 <= j - 1 <= (len(a[i]) - 1) and a[i][j - 1] == 0:
                                a[i][j - 1] = court_day2
                            if 0 <= i - 1 <= (len(a) - 1) and a[i - 1][j] == 0:
                                a[i - 1][j] = court_day2
                            if 0 <= j + 1 <= (len(a[i]) - 1) and a[i][j + 1] == 0:
                                a[i][j + 1] = court_day2
                            if 0 <= i + 1 <= (len(a) - 1) and a[i + 1][j] == 0:
                                a[i + 1][j] = court_day2
    return court_day + 1
