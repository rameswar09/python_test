# def demo1(fun):
#     def inner_demo1(*args, **kwargs):
#
#         print("=====Inner_demo1")
#         fun(*args, **kwargs)
#
#     return inner_demo1
#
#
# @demo1
# def fun2(arg1, arg2):
#     print(arg1)
#     print(arg2)
#     print("decorator Print fun2")
#
#
# fun2(10, 20)

# def star(func):
#     def inner(*args, **kwargs):
#         print("*" * 30)
#         func(*args, **kwargs)
#         print("*" * 30)
#     return inner
#
#
# def percent(func):
#     def inner_percent(*args, **kwargs):
#         print("%" * 30)
#         func(*args, **kwargs)
#         print("%" * 30)
#     return inner_percent
#
#
# @star
# @percent
# def printer(msg):
#     print(msg)
#
#
# printer("Hello")


# my_list = [4, 7, 0, 3]
#
# my_itr = iter(my_list)
#
# print(next(my_itr))


# def my_fun():
#     yield 1
#     yield 2
#     yield 3
#
#
# a = my_fun()
# print(next(a))
# print(next(a))
#
# l1 = [1, 2, 3, 4, 54]
# l2 = (x * x for x in l1)


import sys

print(sys.path)
