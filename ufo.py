def UFO(N, data, octal):
    arr_res = []
    for i in data:
        if octal == False:
            pow = 16
        else:
            pow = 8
        res = int(str(i), base = pow)
        arr_res.append(res)
    return arr_res
