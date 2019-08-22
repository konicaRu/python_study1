def MaximumDiscount(N, price):
    price.sort(reverse = True)
    count = 2
    summ_disc = 0
    for i in range(len(price) // 3):
        summ_disc += price[count]
        count += 3
    return summ_disc


