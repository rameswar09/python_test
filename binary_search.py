# def find_search(arr, num):

#     low_index = 0
#     high_index = len(arr)-1
#     while low_index <= high_index:
#         mid = (low_index+high_index)//2
#         if arr[mid] == num:
#             return mid
#         elif arr[mid] < num:
#             low_index = mid+1
#         else:
#             high_index = mid-1

#     return None


# def find_search(arr, low, high, num):
#     mid = (low+high)//2
#     if arr[mid] == num:
#         return mid
#     elif arr[mid] < num:
#         low = mid+1
#         return find_search(arr, low, high, num)
#     else:
#         high = mid-1
#         return find_search(arr, low, high, num)


# def find_search(arr, low, high, num):
#     mid_value = (low+high)//2
#     if arr[mid_value] == num:
#         return mid_value
#     elif arr[mid_value] > num:
#         high = mid_value-1
#         return find_search(arr, low, high, num)
#     elif arr[mid_value] < num:
#         low = mid_value+1
#         return find_search(arr, low, high, num)


# print(find_search([1, 2, 3, 4, 5, 6, 12, 15, 16, 19, 23, 45], 0, 11, 15))


# import re


# def find_value(arr, num):
#     low = 0
#     high = len(arr)-1
#     while(low <= high):
#         mid_value = (low+high)//2
#         if arr[mid_value] == num:
#             return mid_value
#         if arr[mid_value] > num:
#             high = mid_value-1
#         if arr[mid_value] < num:
#             low = mid_value+1


# print(find_value([1, 2, 3, 4, 5, 6, 12, 15, 16, 19, 23, 45], 15))


# def find_first_occurrence(arr, num):
#     low = 0
#     high = len(arr)-1

#     while(low <= high):
#         mid_index = (low+high)//2
#         if arr[mid_index] == num:
#             if mid_index != 0 and arr[mid_index-1] == num:
#                 high = mid_index-1
#             else:
#                 return mid_index
#         elif arr[mid_index] > num:
#             high = mid_index-1
#         elif arr[mid_index] < num:
#             low = mid_index+1
#     return -1


# print(find_first_occurrence([1, 10, 10, 10, 20, 20, 40], 50))

# count = 0


# def count_occurrence_number(arr, num, low, high):
#     if low > high:
#         return
#     mid_ind = (low+high)//2
#     if arr[mid_ind] == num:
#         global count
#         count += 1
#         if mid_ind != len(arr)-1 and arr[mid_ind+1] == num:
#             count_occurrence_number(arr, num, mid_ind+1, high)
#         if mid_ind != 0 and arr[mid_ind-1] == num:
#             count_occurrence_number(arr, num, low, mid_ind-1)

#     elif arr[mid_ind] > num:
#         high = mid_ind-1
#         count_occurrence_number(arr, num, low, high)
#     elif arr[mid_ind] < num:
#         low = mid_ind+1
#         count_occurrence_number(arr, num, low, high)


# count_occurrence_number([0,0,0,1,1,1,1], 1, 0, 6)
# print(count)


def square_root(num):

    low = 0
    high = num

    while(low <= high):
        mid_value = (low+high)//2

        if mid_value*mid_value==num:
            return mid_value
        elif (mid_value*mid_value)<num and ((mid_value+1)*(mid_value+1))>num:
            return mid_value
        elif (mid_value*mid_value)>num:
            high=mid_value-1
        elif(mid_value*mid_value)<num:
            low=mid_value+1

        # if ((mid_value+1)*(mid_value+1)) > num:
        #     high = mid_value-1
        # elif ((mid_value+1)*(mid_value+1)) < num:
        #     low=mid_value+1
        # elif ((mid_value+1)*(mid_value+1)) == num or ((mid_value+2)*(mid_value+2)) > num:
        #     return mid_value+1


print(square_root(102))
