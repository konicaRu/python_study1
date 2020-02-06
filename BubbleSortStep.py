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

def BubbleSortStep(arr):
    count = -1
    for i in range(len(arr)):
        if i == len(arr) - 1 and count == -1:
            return True
        if i == len(arr) - 1:
            return
        if arr[i] > arr[i + 1]:
            count += 1
            inter_index = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = inter_index



