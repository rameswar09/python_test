# def bit_demo(a,b):
#     print(a^b)

# bit_demo(2,4)


# def shift(a,b):
#     print(a>>b)

# shift(33,1)

# def demo(n):
#     print(n>>>1)
#     # print(n<2)

# demo(-2)


def k_bit(n, k):
    if (n & (1 << (k-1))) == 0:
        return False
    else:
        return True


print(k_bit(8,4))