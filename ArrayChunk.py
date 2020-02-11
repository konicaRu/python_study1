def ArrayChunk(m):
    n = m[len(m) // 2]
    ind_supp = len(m) // 2
    i1 = 0
    i2 = len(m) - 1
    while True:
        if m[i1] < n:
            i1 += 1
        if m[i2] > n:
            i2 -= 1
        if i1 == i2 or i1 == i2 - 1 and m[i1] < m[i2]:
            return ind_supp, m
        if m[i1] == n:
            ind_supp = i2
        if m[i2] == n:
            ind_supp = i1
        inter_el = m[i1]
        m[i1] = m[i2]
        m[i2] = inter_el
