def Merge(left_arr, right_arr):
    res_arr = []
    left_index = right_index = 0
    left_long = len(left_arr)
    right_long = len(right_arr)

    for i in range(left_long + right_long):
        if left_index < left_long and right_index < right_long:
            if left_arr[left_index] <= right_arr[right_index]:
                res_arr.append(left_arr[left_index])
                left_index += 1
            else:
                res_arr.append(right_arr[right_index])
                right_index += 1
        elif left_index == left_long:
            res_arr.append(right_arr[right_index])
            right_index += 1
        elif right_index == right_long:
            res_arr.append(left_arr[left_index])
            left_index += 1

    return res_arr


def MergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left_arr = MergeSort(arr[:mid])
    right_arr = MergeSort(arr[mid:])

    return Merge(left_arr, right_arr)

a = [26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(MergeSort(a))