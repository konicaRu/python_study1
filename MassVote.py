def MassVote(N, Votes):
    summ_pec = 0
    pecent = []
    for i in Votes:
        summ_pec += i
    for i in Votes:
        pecent.append(float('{:.2f}'.format(i / (summ_pec / 100))))
    count = 0
    count1 = 0
    for i in pecent:
        if i == max(pecent):
            count1 += 1
            if count1 == 2:
                return 'no winner'
    for i in pecent:
        count += 1
        if i == max(pecent) and i >= 50:
            return 'majority winner %s' % count
        if i == max(pecent) and i < 50:
            return 'minority winner %s' % count
