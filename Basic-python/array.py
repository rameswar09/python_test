# max element

# a = [1, 22, 63, 34, 55]
# max = a[0]
# for i in a:
#     if max < i:
#         max = i
# print(max)


# a = [5, 8, 20, 10]


# for i in a:
#     flag = True
#     for j in a:
#         if i < j:
#             flag = False
#             break

#     if flag == True:
#         print(i)
#         break


# a = [10, 10, 10]

# l1 = a[0]
# l2 = -1

# for i in range(1, len(a)):
#     if a[i] == l1:
#         continue
#     if a[i] > l1:
#         l2 = l1
#         l1 = a[i]
#     elif a[i] > l2:
#         l2 = a[i]
# if l2 == -1:
#     print("No second large")
# else:
#     print(l2)


# a = [8, 12, 12, 15]

# flag = True

# for i in range(0, len(a)-1):
#     if a[i] > a[i+1]:
#         flag = False
#         break

# print(flag)


# a = [2, 3, 4, 5, 6]
# temp=[]

# for i in reversed(range(len(a))):
#     temp.append(a[i])

# print(temp)
# i = 0
# j = len(a)-1
# while(i < j):
#     temp = a[i]
#     a[i] = a[j]
#     a[j] = temp
#     i += 1
#     j -= 1

# print(a)


a = [10, 20, 20, 20, 30, 30, 30, 30]

# temp = []

# for i in range(len(a)):
#     if i == 0:
#         temp.append(a[i])
#     if a[i] != temp[len(temp)-1]:
#          temp.append(a[i])

# print(temp)


# for i in range(len(a)):
#     if i == 0:
#         print(a[i])
#         continue
#     if a[i] != a[i-1]:
#         print(a[i])
# a=[10,10,10,20]
# j = 0

# for i in range(len(a)):
#     if i == 0:
#         a[j] = a[i]
#         j += 1
#         continue
#     if a[i] != a[i-1]:
#         a[j] = a[i]
#         j += 1

# print(a)


# a = [7, 10, 4, 3, 6, 5, 2]
# number=-1
# for i in reversed(range(len(a))):
#     if a[i]>number:
#         print(a[i])
#         number=a[i]


a = [7, 9, 5, 6, 3, 2, 17]

min_v = a[0]  # 30
res = a[1] - a[0]  # -20
for i in range(1, len(a)):
    if a[i] - min_v > res:
        res = a[i] - min_v
    else:
        min_v = min(min_v, a[i])

print(res)
