def ShopOLAP(N, items):
    res_dic = {}
    res_arr = []
    name_good = ''
    name_dic = ''
    num_good = ''
    count = 0
    for i in range(len(items)):
        for j in range(len(items[i])):
            if items[i][j] != ' ':
                name_good += items[i][j]
            if items[i][j] == ' ':
                name_dic = name_good
                count += 1
            if count == 1 and '0' <= items[i][j] <= '9':
                num_good += items[i][j]
        if name_dic in res_dic:
            res_dic[name_dic] += int(num_good)
            name_good = ''
            num_good = ''
            count = 0
        if name_dic not in res_dic:
            res_dic[name_dic] = int(num_good)
            name_good = ''
            num_good = ''
            count = 0
    for key, value in res_dic.items():
        res_arr.append(key)
        res_arr.append(str(value))
    res_arr_1 = []
    res_arr_2 = []
    item = ''
    sum = ''
    count_sum = 0
    for i in range(0, len(res_arr), 2):
        sum += res_arr[i] + ' ' + str(res_arr[i + 1])
        res_arr_1.append(sum)
        sum = ''
    res_arr_1.sort(reverse=True, key = lambda x: int(x.rsplit(' ',1)[1]))
    return res_arr_1