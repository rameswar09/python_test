def selection_sort(arr):
    for i in range(len(arr)):
        min_value = arr[i]
        min_ind = i
        for j in range(i + 1, len(arr)):
            if arr[j] < min_value:
                min_value = arr[j]
                min_ind = j
        temp = arr[i]
        arr[i] = arr[min_ind]
        arr[min_ind] = temp
    print(arr)


selection_sort([2, 1, 10, 7, 3, 5, 14, 12, 13, 45, 20, 21])
