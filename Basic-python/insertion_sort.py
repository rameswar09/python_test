def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    print(arr)


insertion_sort([2, 1, 10, 7, 3, 5, 14, 12, 13, 45, 20, 21])
