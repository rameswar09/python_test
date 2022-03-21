arr = [4, 3, 1, 2, 10, 9, 8]


def bubble_sort(ar):
    for i in range(len(ar)):
        swapped = False
        for j in range(len(ar) - 1):
            if ar[j] > ar[j + 1]:
                temp = ar[j]
                ar[j] = ar[j + 1]
                ar[j + 1] = temp
                swapped = True
        if not swapped:
            print("Not swapped")
            print(swapped)
            break
    return ar


print(bubble_sort(arr))
