def PatternUnlock(N, hits):
    dial = [[6, 1, 9], [5, 2, 8], [4, 3, 7]]
    keeper = []
    sum = 0
    res = ''
    for i in range(len(hits)):
        if hits[i] == hits[-1]:
            break
        for j in range(len(dial)):
            for k in range(len(dial[j])):
                if hits[i] == dial[j][k] and 0 <= k - 1 <= 2 and dial[j][k - 1] == hits[i + 1]:
                    keeper.append(1)
                if hits[i] == dial[j][k] and 0 <= j + 1 <= 2 and dial[j + 1][k] == hits[i + 1]:
                    keeper.append(1)
                if hits[i] == dial[j][k] and 0 <= k + 1 <= 2 and dial[j][k + 1] == hits[i + 1]:
                    keeper.append(1)
                if hits[i] == dial[j][k] and 0 <= j - 1 <= 2 and dial[j - 1][k] == hits[i + 1]:
                    keeper.append(1)

                if hits[i] == dial[j][k] and 0 <= j - 1 <= 2 and 0 <= k - 1 <= 2 and dial[j - 1][k - 1] == hits[i + 1]:
                    keeper.append(1.41421)
                if hits[i] == dial[j][k] and 0 <= j - 1 <= 2 and 0 <= k + 1 <= 2 and dial[j - 1][k + 1] == hits[i + 1]:
                    keeper.append(1.41421)
                if hits[i] == dial[j][k] and 0 <= j + 1 <= 2 and 0 <= k + 1 <= 2 and dial[j + 1][k + 1] == hits[i + 1]:
                    keeper.append(1.41421)
                if hits[i] == dial[j][k] and 0 <= j + 1 <= 2 and 0 <= k - 1 <= 2 and dial[j + 1][k - 1] == hits[i + 1]:
                    keeper.append(1.41421)
    for i in keeper:
        sum += i
    sum = float('{:.5f}'.format(sum))
    sum = str(sum)
    for i in sum:
        if i != '0' and i != '.':
            res += i
    return res