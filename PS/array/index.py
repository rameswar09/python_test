# array rotation 

# arr=[1,2,3,344,5,6,6]
# temp=[]
# for i in reversed(arr):
#     temp.append(i)
# print(temp)  # space -n time n 

# i=0
# j=len(arr)-1
# while i<j:
#     temp=arr[i]
#     arr[i]=arr[j]
#     arr[j]=temp
#     i+=1
#     j-=1


# print(arr)

# ********************************************************
# d=17

# actuallyRoat = d%len(arr)
# print(actuallyRoat)


# def revFun(arr):
#     i=0
#     j=len(arr)-1
#     while i<j:
#         temp=arr[i]
#         arr[i]=arr[j]
#         arr[j]=temp
#         i+=1
#         j-=1

# revFun(1,2)
# revfun() 
# revFun()

# ****************************************************
arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]


# def searchFun(arr,i,j,key):
#     mid =(i+j)//2
#     if arr[mid]==key:
#         return mid
#     if key<arr[mid]:
#         if arr[i]<=key<arr[mid]:
#             j=mid-1
#         else:
#             i=mid+1
#         return searchFun(arr,i,j,key)
#     if arr[mid]<key:
#         if arr[mid]<key<=arr[j]:
#             i=mid+1
#         elif arr[mid-i]>arr[mid]:
#             j=mid-1
#         else:
#             i=mid+1
#         return searchFun(arr,i,j,key)


# print(searchFun(arr,0,len(arr)-1,1))


def fun(arr):
    low = 0
    i = 0
    j = len(arr) - 1
    while i <= j:
        if i == j:
            return arr[i]
        mid = (i + j) // 2
        if arr[mid] < arr[j]:
            if arr[mid] < arr[mid - 1]:
                low = arr[mid]
                return low
            else:
                j = mid - 1
        elif arr[mid] > arr[j]:
            i = mid + 1


# print(fun([5,6,7,8,1,2,3,4,5]))


count = 0


def checkPairSum(arr, key):
    global count
    l = fun(arr)
    r = l + 1
    while l != r:
        if arr[l] + arr[r] == key:
            count += 1
            if r == 0:
                r = len(arr) - 1
            else:
                r -= 1
            if l == len(arr) - 1:
                l = 0
            else:
                l += 1
        if arr[l] + arr[r] > key:
            if r == 0:
                r = len(arr) - 1
            else:
                r -= 1
        if arr[l] + arr[r] < key:
            if l == len(arr) - 1:
                l = 0
            else:
                l += 1
