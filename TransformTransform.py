def TransformTransform(A, N):
    C = []
    tmp = []  # временный массив
    for i in range(len(A)):
        for j in range(0, len(A) - i):
            k = i + j
            for h in range(j, k+1):  # перебираем А в заданном диапазоне
                tmp.append(A[h])  # добавляем во временный архив
            C.append(max(tmp))  # добавляем в В макс значение из тмп
            tmp = []  # обнуляем временный массив
    i = 0
    j = 0
    k = 0
    h = 0
    B = []
    tmp = []  # временный массив
    for i in range(len(C)):
        for j in range(0, len(C) - i):
            k = i + j
            for h in range(j, k + 1):  # перебираем А в заданном диапазоне
                tmp.append(C[h])  # добавляем во временный архив
            B.append(max(tmp))  # добавляем в В макс значение из тмп
            tmp = []  # обнуляем временный массив
    if sum(B) % 2 == 0:
        return True

