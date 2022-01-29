# def print_loop(n):
#     for i in range(n+1):
#         print(i)
# print_loop(100)


# def print_loop(n):
#     for i in range(10, n+1,2*7):
#         print(i)


# print_loop(20)


def print_loop(n):
    for i in range(1, n):
        if i*i > 100:
            return
        print(i)


print_loop(1123)
