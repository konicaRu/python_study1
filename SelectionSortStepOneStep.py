def SelectionSortStep(arr, b):
    count = b + 1
    index = -1
    dig_index = arr[b + 1]
    for i in range(count, (len(arr))):
        if arr[i] < dig_index:
            dig_index = arr[i]
            index = i
    if index == -1:
        index = b + 1
    if arr[b] > dig_index:
        inter_value = arr[b]
        arr[b] = dig_index
        arr[index] = inter_value
    return arr


print(SelectionSortStep([4, 3, 1, 2, 5], 1))
