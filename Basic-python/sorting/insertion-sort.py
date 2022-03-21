ar = [1, 1, 1, 1, 11, 11, 1, 1, 1, 1]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        ele = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > ele:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = ele
    # for i in range(1, len(arr)):
    #     ele = arr[i]
    #     if arr[i] < arr[i - 1]:
    #         key = 0
    #         for j in reversed(range(i)):
    #             if arr[j] > ele:
    #                 arr[j + 1] = arr[j]
    #             elif arr[j] <= ele:
    #                 key = j + 1
    #                 break
    #         arr[key] = ele
    return arr


print(insertion_sort(ar))
