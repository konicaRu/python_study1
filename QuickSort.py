def QuickSort(m, i1, i2):
    if i1 == i2:
        return
    else:
        left = i1
        right = i2
        if (left + right + 1)//2 > len(m) - 1:
            return
        n = m[(left + right + 1) // 2]
        ind_supp = (left + right + 1) // 2
        while i1 <= i2:
            while m[i1] < n:
                i1 += 1
            while m[i2] > n:
                i2 -= 1
            if i1 == i2 - 1 and m[i1] > m[i2]:
                m[i1], m[i2] = m[i2], m[i1]  # меняем местами элементы списка A[i], A[j] = A[j], A[i]
                n = m[(left + right + 1) // 2]
                ind_supp = (left + right + 1) // 2
                i1 = left
                i2 = right
                continue
            if i1 == i2 or i1 == i2 - 1 and m[i1] < m[i2]:
                QuickSort(m, left, ind_supp - 1)
                return QuickSort(m, ind_supp + 1, right)
            if m[i1] >= n and m[i2] <= n:
                if m[i1] == n:
                    ind_supp = i2
                if m[i2] == n:
                    ind_supp = i1
                m[i1], m[i2] = m[i2], m[i1]  # меняем местами элементы списка A[i], A[j] = A[j], A[i]
