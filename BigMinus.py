def BigMinus(s1, s2):
    dict_num = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}  # делаем словарь где
    sum_1 = 0  # значению цифрового символа соответствует число
    sum_len1 = len(s1)
    for i in s1:
        sum_len1 -= 1
        for j in dict_num:
            if i == j:
                sum_1 += dict_num[j] * (10 ** (sum_len1))  # преобразуем строку s1 в число sum_1
    sum_2 = 0
    sum_len2 = len(s2)
    for i in s2:
        sum_len2 -= 1
        for j in dict_num:
            if i == j:
                sum_2 += dict_num[j] * (10 ** (sum_len2))  # преобразуем строку s2 в число sum_2
    res1 = sum_1 - sum_2  # узнаем  разницу res1 = sum_1 - sum_2
    if res1 < 0:
        res1 = res1 * -1
    if res1 == 0:
        return res1
    res1_tmp = res1
    len_res1 = 0  # узнаем количество знаков в результате разницы res1 = sum_1 - sum_2
    while res1_tmp:  # узнаем количество знаков в результате разницы res1 = sum_1 - sum_2
        len_res1 += 1
        res1_tmp //= 10
    dict_str = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
    sum_str = ''
    for i in range(len_res1):
        len_res1 -= 1
        res2 = (res1 // (10 ** (len_res1))) % 10
        for j in dict_str:
            if res2 == j:
                sum_str += dict_str[j]

    return sum_str
