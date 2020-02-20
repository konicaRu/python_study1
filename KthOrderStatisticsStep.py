def KthOrderStatisticsStep(arr, left, right, k):
    arr_median = []
    end = []
    end_left = left
    while left + 5 <= len(arr) - 1:
        InsertionSort(arr, left, left + 5)
        arr_median.append(arr[left + 2])
        left += 5
    InsertionSort(arr_median, 0, len(arr_median))
    s = arr_median[len(arr_median)//2]
    for i in range(len(arr)):
        if arr[i] == s:
            if k == i:
                end.append(i)
            if k > i:
                end.append(i)
                end.append(right)
            if k < i:
                end.append(end_left)
                end.append(i)
    return end




def InsertionSort(arr, left, right):
    for i in range((left + 1), right):
        new_el = arr[i]
        j = i - 1
        while j >= left and arr[j] > new_el:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = new_el
