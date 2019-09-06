def TransformTransform(A, N):
    C = []
    tmp = []  # временный массив
    for i in A:
        for j in range(len(A) - (i - 1)):
            k = i + j
            if k + 1 > len(A):  # если к превысит диапазан массива А
                k = len(A) - 1  # приводим к к длинне массива А
            for h in range(j, k + 1):  # перебираем А в заданном диапазоне
                tmp.append(A[h])  # добавляем во временный архив
            C.append(max(tmp))  # добавляем в В макс значение из тмп
            tmp = []  # обнуляем временный массив
    i = 0
    j = 0
    k = 0
    h = 0
    B = []
    tmp = []  # временный массив
    for i in C:
        for j in range(len(C) - (i - 1)):
            k = i + j
            if k + 1 > len(C):  # если к превысит диапазан массива А
                k = len(C) - 1  # приводим к к длинне массива А
            for h in range(j, k + 1):  # перебираем А в заданном диапазоне
                tmp.append(C[h])  # добавляем во временный архив
            B.append(max(tmp))  # добавляем в В макс значение из тмп
            tmp = []  # обнуляем временный массив
    if sum(B) % 2 == 0:
        return True
