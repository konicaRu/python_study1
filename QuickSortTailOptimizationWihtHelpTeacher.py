def ArrayChunk(m, i1, i2):
    n = m[i2]
    ind_supp = i2
    while True:
        while m[i1] < n:
            i1 += 1
        while m[i2] > n:
            i2 -= 1
        if i1 == i2 - 1 and m[i1] > m[i2]:
            m[i1], m[i2] = m[i2], m[i1]
            n = m[len(m) // 2]
            ind_supp = len(m) // 2
            i1 = 0
            i2 = len(m) - 1
            continue
        if i1 == i2 or i1 == i2 - 1 and m[i1] < m[i2]:
            return ind_supp
        if m[i1] >= n and m[i2] <= n:
            if m[i1] == n:
                ind_supp = i2
            if m[i2] == n:
                ind_supp = i1
            m[i1], m[i2] = m[i2], m[i1]


def QuickSort(m, i1, i2):
    while i1 < i2:
        ind_supp = ArrayChunk(m, i1, i2)
        QuickSort(m, i1, ind_supp - 1)
        i1 = ind_supp + 1
