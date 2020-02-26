def MergeSort(arr):
    res_arr = []
    left_index = right_index = 0
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    QuickSort(arr, 0, mid)
    QuickSort(arr, mid + 1, len(arr) - 1)
    left_long = len(arr[0:mid + 1])
    right_long = len(arr[mid: len(arr) - 1])
    #for i in range(left_long + right_long - 1):# было без -1
    while left_index < left_long and right_index + left_long <= len(arr) - 1:
            if arr[left_index] < arr[right_index + left_long]:
                res_arr.append(arr[left_index])
                left_index += 1
                if len(res_arr) == len(arr):
                    return res_arr
            if arr[left_index] >= arr[right_index + left_long]:
                res_arr.append(arr[right_index + left_long])
                right_index += 1
                if len(res_arr) == len(arr):
                    return res_arr
    while left_index == left_long:
            res_arr.append(arr[right_index + left_long])
            right_index += 1
            if right_index + left_long > len(arr) - 1:
                return res_arr
    while right_index + left_long == len(arr):# было len(arr) - 1
            res_arr.append(arr[left_index])
            left_index += 1
            if len(res_arr) == len(arr):
                return res_arr
    return res_arr


def QuickSort(m, i1, i2):
    if i1 == i2:
        return m
    else:
        left = i1
        right = i2
        if (left + right + 1) // 2 > len(m) - 1:
            return
        n = m[(left + right + 1) // 2]
        ind_supp = (left + right + 1) // 2
        while i1 <= i2:
            while m[i1] < n:
                i1 += 1
            while m[i2] > n:
                i2 -= 1
            if i1 == i2 - 1 and m[i1] > m[i2]:
                m[i1], m[i2] = m[i2], m[i1]  # меняем местами элементы списка A[i], A[j] = A[j], A[i]
                n = m[(left + right + 1) // 2]
                ind_supp = (left + right + 1) // 2
                i1 = left
                i2 = right
                continue
            if i1 == i2 or i1 == i2 - 1 and m[i1] < m[i2]:
                QuickSort(m, left, ind_supp - 1)
                return QuickSort(m, ind_supp + 1, right)
            if m[i1] >= n and m[i2] <= n:
                if m[i1] == n:
                    ind_supp = i2
                if m[i2] == n:
                    ind_supp = i1
                m[i1], m[i2] = m[i2], m[i1]  # меняем местами элементы списка A[i], A[j] = A[j], A[i]
        return m

a = [2, 1, 10]
#a = [2, 1, 10, 11]
#a = [6, 5, 8, 4, 2, 1, 3]
#a = [2, 1, 3, 4, 8, 5, 6]

print(MergeSort(a))
