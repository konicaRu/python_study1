def QuickSort(m, i1, i2 ):
    if i1 == i2:
        return
    else:
        left = i1
        right = i2
        n = m[(i1 + i2 + 1) // 2]
        ind_supp = (i1 + i2 + 1) // 2
        while True:
            if m[i1] < n:
                i1 += 1
            if m[i2] > n:
                i2 -= 1
            if i1 == i2 - 1 and m[i1] > m[i2]:
                m[i1], m[i2] = m[i2], m[i1] # меняем местами элементы списка A[i], A[j] = A[j], A[i]
                i1 = left
                i2 = right
                n = m[(i1 + i2 + 1) // 2]
                ind_supp = (i1 + i2 + 1) // 2
                continue
            if i1 == i2 or i1 == i2 - 1 and m[i1] < m[i2]:
                QuickSort(m, left, ind_supp - 1 )
                QuickSort(m, ind_supp + 1, right)
            if m[i1] >= n and m[i2] <= n:
                if m[i1] == n:
                    ind_supp = i2
                if m[i2] == n:
                    ind_supp = i1
                m[i1], m[i2] = m[i2], m[i1] # меняем местами элементы списка A[i], A[j] = A[j], A[i]
