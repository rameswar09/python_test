# def bubble_sort(arr):
#     for i in range(len(arr)):
#         swap_flag = False
#         for j in range(1, len(arr)-i):
#             if arr[j] < arr[j-1]:
#                 temp = arr[j-1]
#                 arr[j-1] = arr[j]
#                 arr[j] = temp
#                 swap_flag = True
#         if swap_flag == False:
#             break
#     print(arr)


def bubble_sort(arr):
    for i in range(len(arr)):
        is_swapped = False
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
        if not is_swapped:
            break
    print(arr)


bubble_sort([2, 1, 10, 7, 3, 5, 14, 12, 13, 45, 20, 21])
