def Unmanned(L, N, track):
    color = ''
    dist_gen = 0
    gen_count = 0  # общий счетчик ходов
    for k in range(len(track)):  # отрезков действия столько сколько светофоров
        time_light = 0  # счетчик горения светофора? обнуляем при переходе к след светофору
        wait_time = 0  # время ожидания на светофоре
        time_drive = 0
        while True:
            time_drive += 1
            gen_count += 1
            time_light += 1  # сначала загорается красный
            if time_light > track[k][1] + track[k][2]:  # зацикливаем бесконечное горение светоф
                time_light = 1
            if time_light <= track[k][1]:
                color = 'red'  # то горит красный
            if time_light > track[k][1] and time_light <= track[k][1] + track[k][2]:
                color = 'green'
            if color == 'green' and k == 0 and len(track) > 1:
                dist_gen = track[k][0] + wait_time + (track[k + 1][0] - track[k][0])
                break
            if gen_count > track[k][0] and color == 'red' and k == 0:  # k==0 заглушка для работы только на 1 светофоре
                wait_time += 1  # необходимо сделать чтобы было 2
            if time_drive > dist_gen and color == 'red' and k > 0:
                wait_time += 1
            if time_drive >= dist_gen and color == 'green' and k < len(track) - 1:
                dist_gen = dist_gen + wait_time + (track[k + 1][0] - track[k][0])
                break
            if time_drive >= dist_gen and color == 'green' and k == len(track) - 1 and len(track)>1:
                dist_gen = dist_gen + wait_time + (L - track[k][0])
                return dist_gen
            if color == 'green' and len(track) == 1:
                dist_gen = track[k][0] + wait_time + (L - track[k][0])
                return dist_gen
