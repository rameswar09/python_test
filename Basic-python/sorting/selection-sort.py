# ar = [11, 13, 12, 3, 4, 2, 6, 15, 5, 9]
ar = [1, 1, 1, 1, 1, 1]


def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_ind = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_ind]:
                min_ind = j
        temp = arr[i]
        arr[i] = arr[min_ind]
        arr[min_ind] = temp
    return arr


print(selection_sort(ar))
