
# def factorial(n):
#     res = 1
#     for i in reversed(range(1,n+1)):
#         # res = res*i
#         print(i)
#     return res


# print(factorial(10))


# for i in reversed(range(1, 90,10)):
#     print(i)


# print ("ram")


# def factorial(n):
#     if n == 0:
#         return 1
#     return n*factorial(n-1)


# print(
#     factorial(10))


# def count_zero(n):
#     res = 1
#     for i in range(1, n+1):
#         res *= i
#     count = 0
#     print(res)
#     while(res % 10 == 0):
#         count += 1
#         res = res//10
#     print(count)

# count_zero(45)


# def count_zero(n):
#     total=0
#     i=5
#     while(n/i>=1):
#         total+=(n//i)
#         i*=5
#     print(total)


# count_zero(45)

import math


def gcd(a, b):
    min_number = min(a, b)

    while(min_number > 0):
        if a % min_number == 0 and b % min_number == 0:
            break
        else:
            min_number -= 1
    return min_number


print(gcd(100,200))
