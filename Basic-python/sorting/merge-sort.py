# arr1 = [1, 4, 7, 9]
# arr2 = [2, 3, 5, 8]
arr1 = [1, 4, 7, 9, 10, 11, 2, 3, 5, 8, 10]
m = (0 + len(arr1) - 1) // 2
# print(m)


def merge(arr, l, m, r):
    left_array = []
    right_array = []
    for i in range(l, m + 1):
        left_array.append(arr[i])
    for i in range(m + 1, r + 1):
        right_array.append(arr[i])
    # print(left_array)
    # print(right_array)
    i = 0
    j = 0
    k = l
    while i < len(left_array) and j < len(right_array):
        if left_array[i] <= right_array[j]:
            arr[k] = left_array[i]
            i += 1
            k += 1
        else:
            arr[k] = right_array[j]
            j += 1
            k += 1
    while i < len(left_array):
        arr[k] = left_array[i]
        i += 1
        k += 1
    while j < len(right_array):
        arr[k] = right_array[j]
        j += 1
        k += 1
    # print(arr)


def merge_sort(arr, l, r):
    if l < r:
        mid = (l + r) // 2
        merge_sort(arr, l, mid)
        merge_sort(arr, mid + 1, r)
        merge(arr, l, mid, r)


merge_sort(arr1, 0, len(arr1) - 1)
print(arr1)

# merge(arr1, 0, m, len(arr1)-1)
