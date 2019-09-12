def Keymaker(k):
    arr_moff = [0 for i in range(k+1)]
    count = 0
    line = ''
    for i in range(len(arr_moff) - 1):
        count += 1
        for j in range(0, len(arr_moff), count):
            if arr_moff[j] == 0:
                arr_moff[j] = 1
            else:arr_moff[j] = 0
    arr = arr_moff[1:]
    for i in arr:
        line += str(i)

    return line
