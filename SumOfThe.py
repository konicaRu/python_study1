def SumOfThe(N, data):
    summ = 0
    court = -1
    for j in range(len(data)):
        court += 1
        for i in range(len(data)):
            summ += data[i]
        summ -= data[court]
        if summ == 0:
            return data[court]
        if summ == data[court]:
            return summ
        if summ != data[court]:
            summ = 0
