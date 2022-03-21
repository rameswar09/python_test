# ar1 = [3, 5, 10, 10, 10, 15, 15, 20]
# ar2 = [5, 10, 10, 15, 30]

ar1 = [1, 1, 3, 3, 3]
ar2 = [1, 1, 1, 1, 3, 5, 7]


def intersection(arr1, arr2):
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            if i == 0 and j == 0:
                print(arr1[i])
                i += 1
                j += 1
            elif arr1[i] == arr1[i - 1] and arr2[j] == arr2[j - 1]:
                i += 1
                j += 1
            else:
                print(arr1[i])
                i += 1
                j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1


intersection(ar1, ar2)
