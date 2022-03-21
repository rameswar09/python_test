def merge_sort(arr1, arr2):
    i = 0
    j = 0
    min_length = min(len(arr1), len(arr2))
    while min_length > 0:
        if arr1[i] >= arr2[j]:
            print(arr2[j])
            j += 1
        if arr1[i] < arr2[j]:
            print(arr1[i])
            i += 1
        min_length -= 1

    while i < len(arr1):
        print(arr1[i])
        i += 1
    while j < len(arr2):
        print(arr2[j])
        j += 1


merge_sort([10, 14, 18, 19, 21], [1, 2, 3, 15, 17, 20])
