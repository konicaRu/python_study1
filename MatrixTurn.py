def MatrixTurn(M, N, T):
    arr_mtrx = []
    count = 0
    for i in range(M):
        arr_mtrx.append([])# создаем вложенный массив
        count += 1
        for j in range(count,N+count):# заполняем значениями со сдвигом на count
            arr_mtrx[i].append(j)# добавляем в массив
    legh_line = len(arr_mtrx[0])
    num_line = len(arr_mtrx)
    for j in range(T):
        gen_leght = len(arr_mtrx) * len(arr_mtrx[0])  # общая длинна массива
        read_field = -1
        while gen_leght > 0:
            read_field += 1
            tmp_stor = arr_mtrx[read_field + 1][read_field]
            for i in range(read_field, legh_line - read_field):  # переставляем верхнюю строку
                tmp_stor1 = arr_mtrx[read_field][i]
                arr_mtrx[read_field][i] = tmp_stor
                tmp_stor = tmp_stor1
                gen_leght -= 1
            for i in range(1 + read_field, num_line - read_field):  # переставляем правый столбец
                tmp_stor1 = arr_mtrx[i][legh_line - (read_field + 1)]
                arr_mtrx[i][legh_line - (read_field + 1)] = tmp_stor
                tmp_stor = tmp_stor1
                gen_leght -= 1
            for i in range(legh_line - (read_field + 2), read_field - 1, -1):  # переставляем нижнюю строку
                tmp_stor1 = arr_mtrx[num_line - (read_field + 1)][i]
                arr_mtrx[num_line - (read_field + 1)][i] = tmp_stor
                tmp_stor = tmp_stor1
                gen_leght -= 1
            for i in range(num_line - (read_field + 2), read_field, -1):  # переставляем левый столбец
                tmp_stor1 = arr_mtrx[i][read_field]
                arr_mtrx[i][read_field] = tmp_stor
                tmp_stor = tmp_stor1
                gen_leght -= 1
    return arr_mtrx
